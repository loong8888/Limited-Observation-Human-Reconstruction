# Contributing

Please contribute through an issue or a pull request after the repository is published.

## Add or Correct a Paper

1. Provide the full title and an official publisher, arXiv, author-project, or implementation link.
2. Add or update a record in `data/papers.json` and its BibTeX in `data/references.bib`.
3. Propose inventory membership in `data/inventories.json` with a mechanism-based explanation. Keep hybrid and boundary cases explicit.
4. State the source for venue/year and distinguish preprints from accepted publications.
5. Run `python3 scripts/build.py` and `python3 scripts/validate.py`.

Do not guess project URLs, paper acceptance, code availability, or reconstruction capabilities. Missing information is preferable to invented metadata. Publication-year changes should preserve the source history in the pull request.

## Add a Tool or Dataset

Use the official source and explain the connection to limited-observation human reconstruction. Include important restrictions, such as calibrated cameras, a body-model license, or synthetic references. A public code repository is not a license to redistribute its weights or data.

## Scope

We prioritize subject-specific 3D/4D human recovery and compensatory mechanisms under limited observations. Foundational generation, tracking, geometry, and rendering resources are welcome when their role is explicit. Pure animation resources without a reconstruction or prior connection are outside the core inventory.

Be respectful and concise. Do not attach private human data or material you lack permission to share.
