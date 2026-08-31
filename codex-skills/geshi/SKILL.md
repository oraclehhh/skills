---
name: geshi
description: Standardize and repair English academic thesis or manuscript DOCX files with Microsoft Word and EndNote, including paragraph-structure consolidation review, body-style normalization, spacing/indentation policy, caption style audits, author-metadata cleanup, hyphenation checks, and structural/render QA. Use for Times New Roman 12 pt, 1.5 spacing, two-character body indentation, italic Results subheadings, justified References with 0.5-inch hanging indents, blue EndNote citations, complete ADDIN EN.CITE records, one continuous ADDIN EN.REFLIST bibliography, APA 6th formatting, EndNote library/db-id integration, and broken References repair.
---

# Geshi

Format academic DOCX files and preserve EndNote control. Use the bundled formatter for deterministic OOXML changes, then use genuine Microsoft Word and EndNote for bibliography regeneration.

## Required Inputs

Obtain or discover:

- source DOCX and a distinct output path;
- EndNote `.enl` library when bibliography management is required;
- required EndNote `db-id`;
- citation color, default `0000FF`;
- output font, size, spacing, and indentation, defaulting to Times New Roman, 12 pt, 1.5 lines, and two characters;
- an explicit paragraph policy: choose one body style, one body-after spacing value, and one first-paragraph rule before formatting. Do not infer these from whichever source paragraph happens to be first;
- requested citation style, defaulting to APA 6th when specified by the user.

Never overwrite the only source. Create a timestamped backup before native Word or EndNote updates.

## Project Profile

Discover these values at runtime from the user's task, the document's existing citation fields, and the EndNote library — do not hardcode them. The concrete values below are a worked example from one eye-tracking thesis, kept only to show the expected shape:

- EndNote library: discovered from the task (example: `C:\Users\...\Lib_0812.enl`) with a matching `Lib_0812.Data` directory;
- EndNote `db-id`: read from the existing `<foreign-keys><key>` in the document's `ADDIN EN.CITE` fields, never assumed (example value `fwrv2rpt…`);
- citation field and visible citation color: blue `0000FF`;
- style: APA 6th Edition, not APA 7th; prefer the installed `APA 6th.ens` or the user's `APASixthEditionOfficeOnline.xsl` configuration as appropriate to the active EndNote/Word integration;
- typography: Times New Roman, 12 pt (Chinese small-four equivalent), 1.5 line spacing;
- narrative indent: first line by two characters;
- title-page affiliation block: affiliation paragraphs use Times New Roman 11 pt, italic, centered, zero left/right/first-line/hanging indents; author names governed by the manuscript's title-page style unless the user requests otherwise;
- References alignment and indentation: justified, with a 0.5-inch hanging indent;
- modification note: write a README-style change note to the Desktop when requested;
- preserve the input and write a separately named final DOCX to the Desktop.

## Workflow

1. Inventory the source:
   - count paragraphs, tables, images, `ADDIN EN.CITE`, `ADDIN EN.CITE.DATA`, and `ADDIN EN.REFLIST` fields;
   - locate References, the first and last bibliography entries, and all following tables/figures;
   - record heading, caption, table, and reference styles;
   - report body-style variation, paragraph-after variation, first-line-indent variation, manual line breaks in author metadata, short ordinary prose paragraphs, caption style/length, and suspicious soft-hyphen or non-breaking-hyphen characters;
   - detect replacement characters and mojibake in stored XML.
2. Run the deterministic formatter:

```powershell
python scripts/format_academic_docx.py `
  --input "C:\path\source.docx" `
  --output "C:\path\formatted.docx" `
  --db-id "ENDNOTE_LIBRARY_ID" `
  --citation-color 0000FF `
  --font "Times New Roman" `
  --font-size 12 `
  --line-spacing 1.5 `
  --first-line-chars 2 `
  --apa6
```

3. Read the JSON audit. Stop on missing citation nodes, wrong `db-id`, citation color errors, or conflicting visible typography.
4. If References is EndNote-managed, open the requested `.enl` library and the DOCX in genuine Microsoft Word. Run `Update Citations and Bibliography` on a test copy.
5. Re-audit after update. EndNote may append a new bibliography at the document end while leaving old plain text under References. If so, move the complete new field result below the References heading, delete only the duplicate old reference paragraphs, and keep tables/figures outside the field.
6. Apply local manuscript conventions, including italic Results secondary headings when requested.
7. Save, reopen, structurally audit, render, and inspect every page. Prefer Word PDF export on Windows; use the documents renderer only when available.
8. Write a modification note from `references/modification-note-template.md` when requested or when EndNote repair is material.

## Genuine Word And EndNote

- Do not assume `Word.Application` COM or the default `.docx` association starts Microsoft Word; WPS may hijack both.
- Resolve and launch `WINWORD.EXE` explicitly, commonly `C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE`, with `/x` and the quoted DOCX path.
- Do not use `/a`; it disables add-ins.
- Confirm the `EndNote 2025` ribbon and `Update Citations and Bibliography` control are present before claiming native EndNote processing.
- Open the supplied `.enl` and verify its matching `.Data` directory exists.
- Perform native updates on a test copy. Replace the final output only after structural checks pass.

## Academic Formatting

### Mandatory Heading, Prose, And Formula Rules

- Treat paragraph structure as an editorial unit, not a font-formatting side effect. Within a continuous logical topic, combine adjacent ordinary prose paragraphs into natural 2–6 sentence paragraphs when the source has split them at sentence boundaries. Do not merge across headings, figure/table captions, hypotheses, numbered procedures, citations/fields, list semantics, or a genuine change of analytical topic. Automatic tools may flag candidates, but a human must approve the merge because sentence adjacency alone cannot establish author intent.
- Normalize the body to one canonical narrative style (prefer `Body Text` or the journal's named body style). Map `Normal`, `Normal (Web)`, `First Paragraph`, and copied custom variants to that style while retaining semantic exceptions for headings, captions, references, tables, notes, and title-page metadata. A style-name audit is required after direct formatting; visual similarity is not sufficient.
- Set paragraph spacing explicitly by role. Body paragraphs must share one `spaceAfter` value (normally 0 pt for manuscript submission, or the target journal's stated value); headings, captions, and references may use separate role-specific values, but each role must be internally uniform. Never inherit mixed spacing from source styles.
- Choose and record a first-paragraph policy: either no indent for the first body paragraph after each heading with subsequent body paragraphs indented, or no first-line indents throughout. Apply the policy consistently after every heading, including headings manually formatted with `Normal`.
- Treat a paragraph containing several sentences separated by manual line breaks as one paragraph only when the line breaks are presentational. Split author names, affiliations, and corresponding-author information into separate metadata paragraphs; do not preserve those manual breaks as a single editable author block.
- Use a dedicated `Caption` style for every figure and table caption. Do not center captions by direct formatting alone. Keep captions left-aligned or centered only according to the target journal, use a uniform caption font/spacing, and flag unusually long captions for editorial review rather than forcing arbitrary line breaks.
- Scan the entire document for soft hyphen (`U+00AD`), non-breaking hyphen (`U+2011`), broken hyphenation, and replacement characters. Preserve legitimate compound hyphens, but remove layout-generated soft hyphens and repair visibly corrupted word boundaries before submission.

- Render every manuscript heading and subheading in solid black (`000000`). Headings must be fully flush left: set left, right, first-line, and hanging indentation to zero at both style and paragraph levels. This includes headings manually formatted with `Normal`, not only built-in Heading styles.
- Never apply the narrative first-line indent to any heading or subheading. Audit effective OOXML formatting rather than relying on the visual style name.
- For Nature-style manuscripts, use one uniform 12-pt size for all section-heading levels and distinguish hierarchy only by type style: level 1 is bold roman, level 2 is bold italic, and level 3 is italic roman-weight. Keep all three levels black and flush left with no paragraph indentation.
- Treat the full article title as front matter rather than a section heading. Render the entire title in black bold type, centered, using the manuscript's title size; every title run must be bold, including text split across lines or runs. Do not force it to the 12-pt section-heading size.
- Render the `Abstract` label as a black bold level-1 heading. After the abstract and keywords, begin the manuscript body with the black bold level-1 heading `Introduction`; do not repeat the article title at the start of the body.
- Keep author names in the manuscript's required roman title-page style. Place the affiliation in its own run or paragraph and format only the affiliation as Times New Roman 11 pt italic, black, centered, with no paragraph indentation.
- Do not leave list fragments or one short term per paragraph when the items form a grammatical series. Combine such fragments into one continuous prose paragraph, using commas and a final conjunction. In particular, frequency-band definitions, network-measure definitions, and similar method inventories must not render as one word or one item per line unless the author explicitly requests a list.
- Do not display raw LaTeX, bracketed equations, or pseudo-equation blocks such as `[ RD=... ]` in the final manuscript. Express measure definitions in complete prose unless the author explicitly requests displayed mathematics. Remove the empty or fragment paragraphs left behind by equation conversion.
- Keep visible body prose as complete paragraphs. Reject layouts in which a single ordinary word, abbreviation, or short phrase occupies its own paragraph because of source run splitting, list residue, or conversion artifacts.
- Apply APA statistical italics character by character after all prose consolidation. Italicize only the statistical symbol and preserve roman operators, values, punctuation, correction suffixes, and surrounding narration.
- In Results prose, report adjusted probabilities using italic `p` alone (for example, italic `p` < .001), not visible forms such as `pFDR`, `p_FDR`, or an italic `p` followed by roman `FDR`. State the Benjamini-Hochberg FDR correction once in the statistical-method or figure-note description so the reported `p` values are understood to be corrected.

- Apply Times New Roman, 12 pt, and 1.5 line spacing to visible body text, tables, captions, headers, footers, and references unless the user specifies otherwise.
- Justify all abstract prose and narrative body paragraphs. Apply justified alignment at both the canonical style level and the paragraph level so direct formatting cannot override it. This rule does not apply to the `Abstract` heading, Keywords paragraph, article or section headings, title-page metadata, hypotheses, numbered measure definitions, placeholders, captions, table cells, or notes; retain each excluded role's required alignment.
- Apply a two-character first-line indent to narrative body paragraphs.
- Apply the selected paragraph-after and first-paragraph policy to effective paragraph formatting, not only to the named style definition. Audit both direct paragraph properties and the style tree because direct formatting can silently override a corrected style.
- Do not indent title-page metadata, Abstract labels, Keywords, headings, hypotheses, numbered measure definitions, placeholders, captions, table cells, notes, or References entries.
- Do not use empty paragraphs to create vertical spacing between headings, body paragraphs, captions, placeholders, tables, or figures. Remove empty paragraphs that contain no text, drawing, field, bookmark, section property, or explicit page/line break; control any required spacing through paragraph formatting instead.
- Manuscript-specific exception: preserve exactly one blank paragraph immediately before and after the standalone italic placeholder `[Insert Figure 5]` when the user requires submission-space around that marker. Do not let the general empty-paragraph cleanup remove these two intentional blank lines, and do not apply this exception to other placeholders unless requested.
- Make all manuscript headings flush to their required alignment without paragraph indentation: set left, right, first-line, and hanging indents to zero at both the heading-style level and the paragraph level. Audit manually formatted headings that still use `Normal`, because they can retain the narrative two-character first-line indent even when they visually appear bold or italic.
- Format author affiliations as title-page metadata: Times New Roman 11 pt, italic, centered, and with no left/right/first-line/hanging indentation. Preserve affiliation superscripts and existing author-name formatting unless separately requested.
- Preserve meaningful bold and italics.
- Italicize Results secondary headings when requested, including eye-tracking metric headings, `Gaze Entropy`, `Sensitivity Analyses`, `Exploratory Associations With Behavior`, `Learning Performance`, `Motivation`, and task-level supplementary headings. Do not italicize the primary Results heading or captions solely because of this rule.
- Format every References entry as justified text with a 0.5-inch hanging indent: set `left=720` and `hanging=720` twips, and remove `firstLine`/`firstLineChars`. Never use a positive first-line indent for bibliography entries. Apply this both as direct paragraph formatting and to the `EndNote Bibliography` style so EndNote refreshes do not expose a conflicting style. Preserve EndNote-generated journal-title and volume italics.
- Italicize statistical symbols wherever they function as statistics, including `N`, `M`, `SD`, `SE`, `Mdn`, `Md`, `IQR`, `df`, `p`, `t`, `F`, `H`, `U`, `Z`, `z`, `r`, `R`, `b`, `B`, `d`, `f`, `alpha`/`α`, `beta`/`β`, `delta`/`δ`, `epsilon squared`/`ε²`, and chi-square symbols when present. For this user's manuscripts, italicize Greek statistical symbols as explicitly required. Italicize only the symbol: keep operators, numbers, parentheses, `CI`, and correction suffixes such as `BH` in roman type. Thus format `pBH` with italic `p` and roman `BH`, and format `M (SD)` with both `M` and `SD` italic.
- Format statistical qualifiers as true Word subscripts without a visible underscore. Display `Nmale`, `Mage`, and `SDage` with italic statistical symbols (`N`, `M`, `SD`) followed by roman subscript qualifiers (`male`, `age`). In OOXML, place the qualifier in a separate run with `w:vertAlign w:val="subscript"`; do not leave `_male` or `_age` in visible text, do not italicize the qualifier, and do not render the qualifier at the baseline.
- Audit statistical symbols in the power analysis, participant descriptions, reliability reporting, narrative Results, table headings and cells, table notes, and figure captions. Match by statistical context such as `d =`, `f =`, `α =`, `SD =`, `U =`, `H(`, `ε² =`, `p <`, `z =`, or `M (SD)`; never italicize matching letters inside ordinary words. Perform a character-level audit across adjacent runs because Word can split a single symbol such as `ε²` or `pBH` across multiple runs.
- End statistical italics at the exact symbol boundary. In expressions such as `ε² = .20. Preferred ...`, keep only `ε²` italic; the operator, value, punctuation, and following narrative must be roman. Never let a run containing an italic statistical symbol carry ordinary result narration such as `Preferred exceeded ...`, `did not differ`, or `made fewer errors` in italics. Audit every non-heading italic run containing three or more consecutive alphabetic characters and allow it only when it is an intended term, placeholder, affiliation, or complete statistical abbreviation such as `Mdn` or `IQR`.
- Audit participant descriptors character by character: visible text must contain `Nmale`, `Mage`, and `SDage` without underscores, while the `male`/`age` character spans must have effective subscript formatting and roman type.
- Treat table end-of-cell markers as controls, not visible font-size violations.

## Citation Fields

- For this user's manuscripts, blue EndNote formatting applies to in-text author-year citations only. Both the visible in-text citation and every run of its complete `ADDIN EN.CITE` field instruction/control structure must be blue `0000FF`. Plain blue text without a valid field is not acceptable.

- Preserve existing EndNote record numbers.
- Set every `<foreign-keys><key>` `db-id` to the supplied library ID and use a current Unix timestamp only for newly created or normalized keys.
- Require this complex field structure:
  `w:fldChar(begin)` -> `w:instrText(ADDIN EN.CITE ...)` -> `w:fldChar(separate)` -> visible citation -> `w:fldChar(end)`.
- Require `Author`, `Year`, `RecNum`, `DisplayText`, and a complete `<record>` in every `<Cite>`.
- Require the record nodes listed in `references/endnote-field-schema.md`.
- Match `<DisplayText>` to the visible author-date style, such as `(Author et al., Year)`.
- Color both field-code runs and visible citation runs `0000FF`, unless another color is requested.
- Do not invent DOI, issue, pages, journal, authors, or other metadata. Empty structural nodes are acceptable only when the publication legitimately lacks a value.

## Bibliography Field

- Keep the `References` heading and all visible bibliography entries black `000000`, even when in-text `EN.CITE` fields are blue. Preserve one valid continuous `ADDIN EN.REFLIST` field, but do not color its cached visible bibliography result blue unless the user explicitly and separately requests blue bibliography text.

- Keep one complete References bibliography inside one continuous `ADDIN EN.REFLIST` complex field.
- Reject a field that manages only the first entries while later references are plain text.
- Reject duplicate bibliographies, a second field appended after tables, or tables/figures inside the field result.
- Count visible nonempty bibliography paragraphs between the field separator and end marker. Compare them with distinct records actually cited in the document.
- Do not force uncited records into `EN.REFLIST`. EndNote normally lists only cited records. Report old plain-text entries omitted because they have no matching body citation.
- Prefer native EndNote regeneration from the supplied library. Rebuild OOXML manually only when native update is impossible and complete citation records are available.
- If moving a regenerated field, move the entire begin/instruction/separate/result/end block as one unit. Never create one `EN.REFLIST` field per reference.
- After every EndNote update, re-audit each visible bibliography paragraph and the `EndNote Bibliography` style. Require `w:jc="both"`, `w:ind w:left="720" w:hanging="720"`, and no `w:firstLine` or `w:firstLineChars`.

Read `references/endnote-field-schema.md` before repairing or reconstructing fields.

## APA 6th

- Select an installed APA 6th EndNote style, such as `APA 6th.ens`, when the user requires APA 6th.
- Verify the EndNote Style control after selection and verify regenerated bibliography formatting. Do not infer success from the existence of a style file.
- Do not report APA 6th as complete if Word still shows APA 7th, `Select Another Style`, or an unverified style.
- If UI automation cannot select the style reliably, stop short of claiming success and state the exact remaining manual action.
- Distinguish library metadata defects from style defects. Repeated DOI prefixes such as `https://doi.org/https://doi.org/...`, journal abbreviations, capitalization, or missing issue/pages can originate in the `.enl` record. Report them and avoid silently hard-coding a display-only correction that EndNote will overwrite.

## Encoding And Structure

- Inspect stored OOXML before diagnosing corruption. Correct `Kärnä` and `Martínez-Alcalá` in XML mean a display/refresh problem, not necessarily stored mojibake.
- Scan for `\uFFFD` and known mojibake strings. Preserve correct Unicode throughout extraction, patching, and repackaging.
- Confirm References is followed only by the intended field and then separate paragraphs/objects for later figures and tables.
- Do not describe tables or captions as being inside References solely because they appear after a broken bibliography in linear text extraction; inspect field boundaries and document objects.

## Manuscript Consistency

- Keep Results prose descriptive: report model, statistic, direction, uncertainty, and table/figure location without adding mechanisms.
- Ensure every external interpretation in Discussion has a supporting author-year citation; use the study's own table/figure references for statements describing the present results.
- Keep citation display color uniform across the full manuscript.
- Preserve exact condition labels required by the manuscript, including `P-I`, `N-I`, and `I-A`; do not reintroduce `NP-I` or `A-I`.
- Keep figure axes and legends in English when the manuscript is English. Include visible color legends and requested pairwise significance annotations.
- After editing content, reapply the document-wide typography, spacing, indentation, heading, citation, reference, and caption rules before delivery.

## Adding Citations

1. Verify metadata from the supplied paper, DOI registry, or EndNote record.
2. Reuse an existing DOCX or library record when author, year, and DOI match.
3. Allocate a unique record number only for a genuinely new record.
4. Insert a complete `ADDIN EN.CITE` complex field.
5. Update the bibliography through EndNote rather than adding a detached plain-text entry.

## Delivery Gate

🔴 CHECKPOINT · 🛑 STOP：Do not claim completion until:

- the output reopens in genuine Microsoft Word;
- all requested secondary Results headings are italic;
- all APA statistical symbols are italic in正文, tables, notes, and captions without italicizing surrounding operators or correction suffixes;
- no ordinary narrative phrase is italic because it shares a run with a statistical symbol; long non-heading italic runs have been reviewed explicitly;
- `Nmale`, `Mage`, and `SDage` contain no visible underscores; their qualifiers are roman true subscripts and only `N`, `M`, or `SD` is italic;
- narrative indentation exclusions are correct;
- all heading paragraphs, including manually formatted headings using `Normal`, have zero left/right/first-line/hanging indentation;
- every heading and subheading has effective black `000000` text, with no theme color or inherited accent color;
- no raw LaTeX, bracketed pseudo-equation block, frequency-band fragment, network-measure fragment, or ordinary one-word paragraph remains;
- no unreviewed short ordinary prose paragraph remains inside a continuous method/results topic; the audit reports every candidate and records whether it was merged or intentionally retained;
- body prose uses one canonical narrative style, role-specific caption/reference styles are consistent, and no unexplained `Normal`/`Normal (Web)`/`First Paragraph` mixture remains;
- body paragraph-after spacing and first-paragraph indentation follow the declared policy with zero unexplained exceptions;
- all abstract prose, narrative body paragraphs, and References entries are effectively justified, while headings, Keywords, captions, metadata, tables, notes, and other excluded roles retain their required alignment;
- author names, affiliations, and corresponding-author information are separate metadata paragraphs with no retained manual line-break-only structure;
- all figure/table captions use the dedicated caption style, and unusually long captions plus arbitrary manual line breaks are reported;
- soft-hyphen, broken-hyphenation, replacement-character, and mojibake checks pass;
- no nonstructural empty paragraphs remain between manuscript content blocks; empty paragraphs containing drawings, EndNote field boundaries, bookmarks, section properties, or explicit breaks are preserved;
- `[Insert Figure 5]`, when present under this manuscript profile, has exactly one intentional blank paragraph above and below it;
- title-page affiliation paragraphs are 11 pt italic, centered, and have no paragraph indentation;
- author names remain roman while only affiliation text is 11 pt italic;
- the complete article title is centered, black, and bold across every run and line;
- Nature-style section headings use a uniform 12-pt size, with level 1 bold, level 2 bold italic, and level 3 italic; all remain black and flush left;
- the body begins with `Introduction` after the Abstract/Keywords block, and the article title is not repeated as a body heading;
- visible Results statistics contain no `pFDR`, `p_FDR`, or split italic-`p` plus roman-`FDR` form; corrected probabilities are displayed as italic `p` only, with BH-FDR documented in the method or note;
- citation audit has zero missing nodes, wrong `db-id` values, and color errors;
- exactly one continuous `ADDIN EN.REFLIST` covers all cited bibliography entries;
- every visible in-text citation and its `EN.CITE` instruction/field-control runs are blue `0000FF`;
- the `References` heading and every visible bibliography entry are black `000000`, while exactly one continuous `EN.REFLIST` field remains structurally valid;
- no duplicate plain-text reference list remains;
- every References entry and the `EndNote Bibliography` style use justified alignment and a 0.5-inch hanging indent, with no positive first-line indent;
- figures and tables remain outside the bibliography field;
- Unicode and mojibake checks pass;
- the EndNote style is verified as APA 6th when requested;
- every rendered page is inspected, or the final response explicitly states why rendering was unavailable;
- the modification note records counts, omitted uncited entries, library metadata defects, backups, style status, and remaining limitations.

Never report a partially satisfied gate as complete.
