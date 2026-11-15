# Publication File Guide

## Include in the Public Repository

| Path | Purpose |
| --- | --- |
| README.md | Main navigation and survey description |
| resources/ | Method families, paper index, datasets, tools, and public source audit |
| data/ except audit-cache/ | Bibliography, structured inventories, source links, and reproducible metadata |
| homepage/ | Searchable static catalogue; keep catalogue.js with the HTML, CSS, and JavaScript |
| assets/ | Images and icons referenced by README and homepage, with original license notices |
| LICENSE and LICENSES/ | Scope of the code/documentation licenses and third-party exclusions |
| scripts/ | Rebuild and validate generated pages |
| .gitignore | Prevent local caches and review artifacts from entering commits |

## Included Supporting Files

These are not needed merely to display the catalogue, but are useful for a maintained academic repository and are included in the initial release:

- paper/: accompanying manuscript PDF and citation notes. Keep it if distributing this author-approved PDF; the root LICENSE does not relicense the manuscript.
- CONTRIBUTING.md and .github/: contribution guidance, issue templates, and validation workflow.
- CHANGELOG.md, MAINTAINING.md, and this guide: release history and maintenance instructions.
- resources/reference-audit.md, data/reference_audit.json, data/metadata_corrections.json, and data/provenance.json: compact public traceability, source links, and correction history. Full API responses are retained locally under the ignored audit-cache directory, not published.
- assets/survey-overview.pdf: editable/vector companion to the PNG preview; optional for display.

## Do Not Upload

| Local path | Reason |
| --- | --- |
| BUILD_REPORT.md | Internal completion/review report; excluded by .gitignore |
| RELEASE_CHECKLIST.md | Local approval checklist; excluded by .gitignore |
| data/audit-cache/ | Intermediate downloaded API/page responses; excluded by .gitignore |
| .DS_Store, __pycache__/, *.pyc, .tmp/ | Operating-system, interpreter, and temporary files |
| .git/ | Local Git metadata; never upload as ordinary repository content |

The manuscript's LaTeX build products, icon-comparison v3, screenshots, one-off import/audit scripts, and reference Human-Centric-AI repository are outside this repository and are not included.

## Remaining Placeholder

ARXIV_ID_TO_BE_ADDED is intentional. Replace the placeholder and the corresponding null arxiv_url in data/publication.json after the survey receives its own identifier. Do not use the template paper's arXiv ID.
