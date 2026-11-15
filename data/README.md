# Catalogue Data

We provide the collection in structured formats so that readers can search, reuse, and extend it.

| File | Contents |
| --- | --- |
| `papers.json` | Titles, authors, venues, years, source links, BibTeX, and taxonomy associations |
| `references.bib` | References accompanying our survey and resource collection |
| `inventories.json` | Method and dataset inventories, including mechanisms, representations, and assumptions |
| `paper_links.json` | Paper sources and available PDF, project, and code links |
| `code_links.json` | Selected official implementations used as entry points |
| `tools.json` | Complementary software and collections, with their roles and limitations |

Taxonomy associations indicate where a paper contributes to our discussion, not an exclusive classification. A paper may describe both a method and a dataset. Blank project or code fields mean that no link is provided; they do not establish that an implementation does not exist. Dashes indicate information not reported in the cited source.

## Reuse and Contribute

Each inventory's `headers` defines the meaning and order of its row `cells`. Citation IDs connect entries to `papers.json` and `references.bib`. Please preserve IDs when correcting a record so that links continue to work.

To regenerate our inventories and catalogue after making changes, run these commands from the repository root:

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

Our validation script checks data consistency and repository links. For contributions, please provide the original paper or official project source; see [CONTRIBUTING.md](../CONTRIBUTING.md). License scope is described in [LICENSE](../LICENSE).
