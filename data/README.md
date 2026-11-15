# Data Guide

- `papers.json`: complete imported bibliography; title, authors, year, venue, URL, raw BibTeX, source status, and inventory-group links.
- `inventories.json`: manuscript method/dataset table rows, original table labels, section numbers, summaries, and caveats.
- `references.bib`: the author's supplied bibliography, preserved as a snapshot.
- `tools.json`: complementary tools and collections, with official URLs, purpose, caveat, and link-check date.
- `code_links.json`: selected official implementation URLs keyed by bibliography ID, with check scope and date.
- `provenance.json`: source filenames, hashes, and provenance policy.
- `reference_audit.json`: per-record metadata responses, source evidence, and unresolved conflicts.
- `paper_links.json`: PDF/project/code discovery and access-check status for all 243 records. A blank means not located, not nonexistent. Accessibility alone does not prove official authorship.

A paper's `inventory_groups` records where it appears in the manuscript inventory, not exclusive scientific family membership. A source paper may describe a dataset as well as a method.

`rows[].cells` follows the corresponding `headers` array exactly. Unknown or unreported values remain dashes. Publication metadata is imported rather than independently re-audited here. URLs are DOI links, supplied URLs, or explicit arXiv identifiers; a missing link is never replaced by a guessed URL.
