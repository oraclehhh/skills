#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import time
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
ET.register_namespace("w", W)

HEADING_TEXT = {
    "Introduction", "Experiment 1", "Experiment 2", "Participants and Design",
    "Video Lectures", "Measures", "Learning Performance Tests", "Motivation questionnaire",
    "Motivation Questionnaire", "Data Analysis", "Procedure", "Results", "Learning Performance",
    "Task-Level Supplementary Analysis", "Motivation", "Eye-Tracking Data Collection",
    "Eye-Tracking Data Analysis", "Gaze-Entropy Analysis", "Behavioral Data Analysis",
    "Eye-Tracking Results", "Total Fixation Duration and Total Fixation Count",
    "Proportional Fixation Duration on AOIs", "Proportion of Undirected AOI Transitions",
    "Gaze Entropy", "Sensitivity Analyses", "Exploratory Associations With Behavior",
    "Behavioral Results", "Discussion", "Limitations and Future Directions", "Conclusion",
    "References",
}
REFERENCE_STYLE_IDS = {"EndNoteBibliography", "15"}
CAPTION_STYLE_IDS = {"Caption", "TableCaption", "FigureCaption"}
METADATA_STYLE_IDS = {"Title", "Subtitle", "Author", "FirstParagraph"}


def qn(name):
    return f"{{{W}}}{name}"


def ensure(parent, name, text=None):
    node = parent.find(qn(name))
    if node is None:
        node = ET.SubElement(parent, qn(name))
    if node.text is None and text is not None:
        node.text = text
    return node


def ensure_path(root, path, text=""):
    node = root
    for name in path.split("/"):
        child = node.find(name)
        if child is None:
            child = ET.SubElement(node, name)
        node = child
    if node.text is None:
        node.text = text
    return node


def text_of(p):
    return "".join(x.text or "" for x in p.findall(".//w:t", NS)).strip()


def style_of(p):
    node = p.find("w:pPr/w:pStyle", NS)
    return node.get(qn("val")) if node is not None else ""


def paragraph_spacing_after(p):
    node = p.find("w:pPr/w:spacing", NS)
    if node is None:
        return None
    value = node.get(qn("after"))
    return int(value) if value is not None and value.isdigit() else 0 if value == "0" else None


def has_manual_line_break(p):
    return bool(p.findall(".//w:br", NS))


def soft_hyphen_count(text):
    return text.count("\u00ad")


def is_caption_text(text):
    return bool(re.match(r"^(Figure|Fig\.?|Table)\s+\d+\b", text, re.I))


def is_heading(p):
    return text_of(p) in HEADING_TEXT or style_of(p) in {
        "Heading1", "Heading2", "Heading3", "Heading 1", "Heading 2", "Heading 3",
        "1", "2", "4", "5",
    }


def set_run_format(run, font, half_points, color=None):
    rpr = run.find("w:rPr", NS)
    if rpr is None:
        rpr = ET.Element(qn("rPr")); run.insert(0, rpr)
    fonts = ensure(rpr, "rFonts")
    for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
        fonts.set(qn(attr), font)
    ensure(rpr, "sz").set(qn("val"), str(half_points))
    ensure(rpr, "szCs").set(qn("val"), str(half_points))
    if color:
        ensure(rpr, "color").set(qn("val"), color)


def normalize_record(record, db_id, timestamp):
    recnum = ensure_path(record, "rec-number", "0").text or "0"
    key = ensure_path(record, "foreign-keys/key", recnum)
    key.attrib.setdefault("app", "EN")
    key.set("db-id", db_id)
    key.set("timestamp", timestamp)
    ref_type = ensure_path(record, "ref-type", "17")
    ref_type.attrib.setdefault("name", "Journal Article")
    for path in (
        "contributors/authors/author", "titles/title", "titles/secondary-title",
        "periodical/full-title", "volume", "number", "pages", "dates/year",
        "urls/related-urls/url", "electronic-resource-num",
    ):
        ensure_path(record, path, "")
    doi = (record.findtext("electronic-resource-num") or "").strip()
    url = record.find("urls/related-urls/url")
    if doi and not (url.text or "").strip():
        url.text = "https://doi.org/" + doi.removeprefix("https://doi.org/")


def is_narrative(p, index, in_table):
    text = text_of(p)
    if index < 9 or not text or in_table:
        return False
    if style_of(p) in REFERENCE_STYLE_IDS or style_of(p) in CAPTION_STYLE_IDS:
        return False
    if text in HEADING_TEXT or style_of(p) in {"Heading1", "Heading2", "Heading3", "Heading 1", "Heading 2", "Heading 3", "1", "2", "4", "5"}:
        return False
    if text.startswith(("Abstract:", "Keywords:", "[Insert ", "Figure ", "Table ", "Note.",
                        "Hypothesis 1:", "Hypothesis 2:", "(1)", "(2)", "(3)", "(4)")):
        return False
    return True


def append_text_run(p, text, italic=False):
    r = ET.SubElement(p, qn("r"))
    rpr = ET.SubElement(r, qn("rPr"))
    if italic:
        ET.SubElement(rpr, qn("i")); ET.SubElement(rpr, qn("iCs"))
    t = ET.SubElement(r, qn("t"))
    if text.startswith(" ") or text.endswith(" "):
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text


def italicize_reference_journal_volume(p):
    text = text_of(p)
    m = re.search(r"\(\d{4}\)\.\s+.+?\.\s+(.+?),\s+(\d+)(?=\(|,)", text)
    if not m:
        return False
    ppr = p.find("w:pPr", NS)
    for child in list(p):
        if child is not ppr:
            p.remove(child)
    append_text_run(p, text[:m.start(1)])
    append_text_run(p, text[m.start(1):m.end(2)], italic=True)
    append_text_run(p, text[m.end(2):])
    return True


def patch_document(data, args):
    root = ET.fromstring(data)
    timestamp = str(int(time.time()))
    table_paras = {id(p) for tc in root.findall(".//w:tc", NS) for p in tc.findall(".//w:p", NS)}
    all_body = root.findall(".//w:body//w:p", NS)
    audit = {"narrative_indents": 0, "reference_hanging_indents": 0, "endnote_fields": 0,
             "cite_records": 0, "missing_required_nodes": 0, "wrong_db_id": 0,
             "field_color_errors": 0, "runs_formatted": 0, "paragraphs_formatted": 0,
             "apa6_journal_entries_italicized": 0, "body_style_counts": {},
             "body_after_counts": {}, "short_prose_candidates": [],
             "author_metadata_manual_breaks": [], "caption_style_issues": [],
             "caption_length_candidates": [], "soft_hyphen_count": 0,
             "nonbreaking_hyphen_count": 0, "first_paragraph_policy": args.first_paragraph_policy,
             "body_after_pt": args.body_after_pt}
    half_points = int(round(args.font_size * 2))
    line_twips = int(round(args.line_spacing * 240))
    first_line_twips = int(round(args.first_line_chars * args.font_size * 20))
    hanging_twips = int(round(args.reference_hanging_inches * 1440))

    for index, p in enumerate(all_body):
        text = text_of(p)
        style = style_of(p)
        if text:
            audit["soft_hyphen_count"] += soft_hyphen_count(text)
            audit["nonbreaking_hyphen_count"] += text.count("\u2011")
        if is_caption_text(text):
            if style not in CAPTION_STYLE_IDS:
                audit["caption_style_issues"].append({"index": index, "style": style, "text": text[:160]})
            if len(text) >= args.caption_review_chars:
                audit["caption_length_candidates"].append({"index": index, "chars": len(text), "text": text[:160]})
        if has_manual_line_break(p) and index < args.author_metadata_scan_paragraphs:
            audit["author_metadata_manual_breaks"].append(index)
        if text and is_narrative(p, index, id(p) in table_paras):
            audit["body_style_counts"][style] = audit["body_style_counts"].get(style, 0) + 1
            after = paragraph_spacing_after(p)
            key = str(after) if after is not None else "inherited/unspecified"
            audit["body_after_counts"][key] = audit["body_after_counts"].get(key, 0) + 1
            if len(text) <= args.short_prose_chars:
                audit["short_prose_candidates"].append({"index": index, "chars": len(text), "text": text[:160]})
        if args.apa6 and style_of(p) in REFERENCE_STYLE_IDS:
            audit["apa6_journal_entries_italicized"] += int(italicize_reference_journal_volume(p))
        ppr = p.find("w:pPr", NS)
        if ppr is None:
            ppr = ET.Element(qn("pPr")); p.insert(0, ppr)
        spacing = ensure(ppr, "spacing")
        spacing.set(qn("line"), str(line_twips)); spacing.set(qn("lineRule"), "auto")
        if is_narrative(p, index, id(p) in table_paras):
            spacing.set(qn("after"), str(int(round(args.body_after_pt * 20))))
        audit["paragraphs_formatted"] += 1
        ind = ensure(ppr, "ind")
        if style in REFERENCE_STYLE_IDS:
            ind.set(qn("left"), str(hanging_twips)); ind.set(qn("hanging"), str(hanging_twips))
            ind.attrib.pop(qn("firstLine"), None)
            audit["reference_hanging_indents"] += 1
        elif is_narrative(p, index, id(p) in table_paras):
            previous = all_body[index - 1] if index else None
            first_after_heading = previous is not None and is_heading(previous)
            if args.first_paragraph_policy == "heading-first-no-indent" and first_after_heading:
                ind.attrib.pop(qn("firstLine"), None)
            else:
                ind.set(qn("firstLine"), str(first_line_twips))
            ind.attrib.pop(qn("hanging"), None)
            audit["narrative_indents"] += 1
        else:
            ind.attrib.pop(qn("firstLine"), None)

        active = False; is_endnote = False; field_runs = []; pieces = []
        for run in p.findall("w:r", NS):
            set_run_format(run, args.font, half_points, "000000")
            audit["runs_formatted"] += 1
            fld = run.find("w:fldChar", NS); instr = run.find("w:instrText", NS)
            if fld is not None and fld.get(qn("fldCharType")) == "begin":
                active, is_endnote, field_runs, pieces = True, False, [run], []
                continue
            if not active:
                continue
            field_runs.append(run)
            if instr is not None:
                pieces.append(instr.text or "")
                if "ADDIN EN.CITE" in (instr.text or ""):
                    is_endnote = True
            if fld is not None and fld.get(qn("fldCharType")) == "end":
                instruction = "".join(pieces)
                if is_endnote:
                    for r in field_runs:
                        set_run_format(r, args.font, half_points, args.citation_color)
                    if "<EndNote>" in instruction:
                        audit["endnote_fields"] += 1
                        try:
                            en = ET.fromstring(instruction[instruction.index("<EndNote>"):].strip())
                            for cite in en.findall("Cite"):
                                rec = cite.find("record")
                                if rec is not None:
                                    normalize_record(rec, args.db_id, timestamp)
                                    audit["cite_records"] += 1
                            rebuilt = instruction[:instruction.index("<EndNote>")] + ET.tostring(en, encoding="unicode", short_empty_elements=False)
                            nodes = [n for r in field_runs for n in r.findall("w:instrText", NS)]
                            if nodes:
                                nodes[0].text = rebuilt
                                for n in nodes[1:]: n.text = ""
                        except ET.ParseError:
                            audit["missing_required_nodes"] += 1
                active, is_endnote, field_runs, pieces = False, False, [], []

    return ET.tostring(root, encoding="utf-8", xml_declaration=True), audit


def patch_simple_part(data, args):
    root = ET.fromstring(data)
    half_points = int(round(args.font_size * 2)); line_twips = int(round(args.line_spacing * 240))
    for p in root.findall(".//w:p", NS):
        ppr = p.find("w:pPr", NS)
        if ppr is None:
            ppr = ET.Element(qn("pPr")); p.insert(0, ppr)
        spacing = ensure(ppr, "spacing"); spacing.set(qn("line"), str(line_twips)); spacing.set(qn("lineRule"), "auto")
        for r in p.findall("w:r", NS): set_run_format(r, args.font, half_points, "000000")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def audit_document(data, args, base):
    root = ET.fromstring(data)
    required = ("rec-number", "foreign-keys/key", "ref-type", "contributors/authors/author",
                "titles/title", "titles/secondary-title", "periodical/full-title", "volume", "number",
                "pages", "dates/year", "urls/related-urls/url", "electronic-resource-num")
    complete_fields = records = missing = wrongdb = color_errors = 0
    for p in root.findall(".//w:p", NS):
        active = False; is_endnote = False; runs = []; pieces = []
        for r in p.findall("w:r", NS):
            fld = r.find("w:fldChar", NS); instr = r.find("w:instrText", NS)
            if fld is not None and fld.get(qn("fldCharType")) == "begin":
                active, is_endnote, runs, pieces = True, False, [r], []; continue
            if not active: continue
            runs.append(r)
            if instr is not None:
                pieces.append(instr.text or ""); is_endnote |= "ADDIN EN.CITE" in (instr.text or "")
            if fld is not None and fld.get(qn("fldCharType")) == "end":
                s = "".join(pieces); active = False
                if not is_endnote: continue
                color_errors += int(any((x.find("w:rPr/w:color", NS) is None or x.find("w:rPr/w:color", NS).get(qn("val")) != args.citation_color) for x in runs))
                if "<EndNote>" not in s: continue
                complete_fields += 1
                try: en = ET.fromstring(s[s.index("<EndNote>"):].strip())
                except ET.ParseError: missing += 1; continue
                for cite in en.findall("Cite"):
                    records += 1; rec = cite.find("record")
                    missing += sum(rec is None or rec.find(path) is None for path in required)
                    key = rec.find("foreign-keys/key") if rec is not None else None
                    wrongdb += int(key is None or key.get("db-id") != args.db_id)
    style_counts = {}
    body_after_counts = {}
    short_prose = []
    captions = []
    soft_hyphens = 0
    nonbreaking_hyphens = 0
    paragraphs = root.findall(".//w:body//w:p", NS)
    for index, p in enumerate(paragraphs):
        text = text_of(p)
        style = style_of(p)
        soft_hyphens += soft_hyphen_count(text)
        nonbreaking_hyphens += text.count("\u2011")
        if is_caption_text(text):
            captions.append({"index": index, "style": style, "chars": len(text), "manual_break": has_manual_line_break(p)})
        if text and is_narrative(p, index, False):
            style_counts[style] = style_counts.get(style, 0) + 1
            after = paragraph_spacing_after(p)
            key = str(after) if after is not None else "inherited/unspecified"
            body_after_counts[key] = body_after_counts.get(key, 0) + 1
            if len(text) <= args.short_prose_chars:
                short_prose.append({"index": index, "chars": len(text), "text": text[:160]})
    base.update({"complete_endnote_fields": complete_fields, "cite_records": records,
                 "missing_required_nodes": missing, "wrong_db_id": wrongdb,
                 "field_color_errors": color_errors,
                 "post_format_short_prose_candidates": short_prose,
                 "post_format_short_prose_style_counts": style_counts,
                 "post_format_short_prose_after_counts": body_after_counts,
                 "captions": captions, "soft_hyphen_count": soft_hyphens,
                 "nonbreaking_hyphen_count": nonbreaking_hyphens})
    return base


def main():
    ap = argparse.ArgumentParser(description="Format an academic DOCX and normalize existing EndNote fields.")
    ap.add_argument("--input", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--db-id", required=True)
    ap.add_argument("--citation-color", default="0000FF")
    ap.add_argument("--font", default="Times New Roman")
    ap.add_argument("--font-size", type=float, default=12)
    ap.add_argument("--line-spacing", type=float, default=1.5)
    ap.add_argument("--first-line-chars", type=float, default=2)
    ap.add_argument("--first-paragraph-policy", choices=("heading-first-no-indent", "all-indented"),
                    default="heading-first-no-indent",
                    help="Whether the first narrative paragraph after a heading is unindented or follows the body indent.")
    ap.add_argument("--body-after-pt", type=float, default=0,
                    help="Explicit space-after for ordinary body paragraphs, in points.")
    ap.add_argument("--reference-hanging-inches", type=float, default=.5)
    ap.add_argument("--apa6", action="store_true", help="Apply hanging indents and italicize recognizable journal-title/volume segments.")
    ap.add_argument("--short-prose-chars", type=int, default=180,
                    help="Flag ordinary prose paragraphs at or below this length for human merge review.")
    ap.add_argument("--caption-review-chars", type=int, default=600,
                    help="Flag captions at or above this length for editorial review.")
    ap.add_argument("--author-metadata-scan-paragraphs", type=int, default=12,
                    help="Scan the opening paragraphs for manual line breaks in author metadata.")
    args = ap.parse_args()
    args.citation_color = args.citation_color.upper().removeprefix("#")
    if args.input.resolve() == args.output.resolve():
        raise SystemExit("Input and output must differ; preserve the source.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(args.input, args.output)
    tmp = args.output.with_suffix(".formatting.tmp.docx")
    audit = {}
    with zipfile.ZipFile(args.output, "r") as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml": data, audit = patch_document(data, args)
            elif item.filename.startswith("word/header") or item.filename.startswith("word/footer"):
                data = patch_simple_part(data, args)
            zout.writestr(item, data)
    tmp.replace(args.output)
    with zipfile.ZipFile(args.output) as z:
        final = audit_document(z.read("word/document.xml"), args, audit)
    final.update({"input": str(args.input), "output": str(args.output), "font": args.font,
                  "font_size": args.font_size, "line_spacing": args.line_spacing,
                  "first_line_chars": args.first_line_chars, "citation_color": args.citation_color})
    print(json.dumps(final, ensure_ascii=False, indent=2))
    if final["missing_required_nodes"] or final["wrong_db_id"] or final["field_color_errors"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
