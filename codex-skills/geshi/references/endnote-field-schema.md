# EndNote Field And Bibliography Contract

## Citation Field

An EndNote citation is a Word complex field:

```xml
<w:r><w:fldChar w:fldCharType="begin"/></w:r>
<w:r><w:instrText xml:space="preserve"> ADDIN EN.CITE &lt;EndNote&gt;...&lt;/EndNote&gt;</w:instrText></w:r>
<w:r><w:fldChar w:fldCharType="separate"/></w:r>
<w:r><w:t>(Author et al., 2025)</w:t></w:r>
<w:r><w:fldChar w:fldCharType="end"/></w:r>
```

Each `<Cite>` must contain `Author`, `Year`, `RecNum`, `DisplayText`, and a complete `<record>`.

Required record nodes:

- `rec-number`
- `foreign-keys/key` with `app="EN"`, the requested `db-id`, and Unix `timestamp`
- `ref-type` with its `name` attribute and numeric code
- `contributors/authors/author`
- `titles/title`
- `titles/secondary-title`
- `periodical/full-title`
- `volume`, `number`, `pages`
- `dates/year`
- `urls/related-urls/url`
- `electronic-resource-num`

Use the complete instruction form:

```text
ADDIN EN.CITE <EndNote><Cite>...complete record...</Cite></EndNote>
```

Color all runs belonging to the field, including displayed citation text, with `w:color w:val="0000FF"` when blue citations are required.

Never fabricate missing bibliographic values. Keep an empty node when the source legitimately has no value.

## Bibliography Field

A managed bibliography is one complex field whose instruction contains:

```text
ADDIN EN.REFLIST
```

The field must contain:

1. one `w:fldChar` begin marker;
2. the `ADDIN EN.REFLIST` instruction;
3. one `w:fldChar` separate marker;
4. all visible bibliography paragraphs as the cached field result;
5. one `w:fldChar` end marker after the last entry.

The markers may span multiple paragraphs. Audit field depth across paragraph boundaries; do not assume begin and end are in one paragraph.

Valid state:

- exactly one bibliography field;
- every cited reference is inside its result;
- no duplicate plain-text references outside it;
- later table and figure objects start after its end marker.

Invalid states:

- only the first reference is between separator and end;
- some entries are managed and some are plain text;
- a regenerated bibliography is appended after figures/tables;
- old plain-text references remain below References;
- separate `EN.REFLIST` fields are created for individual references;
- uncited references are inserted into the managed field without body citations.

## Native Repair

Prefer genuine Word and the connected EndNote library:

1. open the `.enl` and verify its `.Data` directory;
2. open a test DOCX through `WINWORD.EXE /x` without `/a`;
3. verify the EndNote ribbon;
4. run `Update Citations and Bibliography`;
5. save and close;
6. audit field boundaries and visible entries;
7. if EndNote appended a complete field at the end, move the entire field block under References and delete only the old duplicate reference paragraphs.

## Metadata And Encoding

- Treat duplicated DOI prefixes and journal abbreviations as possible library-record defects.
- Do not rewrite managed result text as a permanent fix; the next EndNote refresh can overwrite it.
- Inspect XML for correct Unicode before diagnosing encoding corruption.
- Scan for replacement characters and known mojibake after every OOXML rewrite.
