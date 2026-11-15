# Maintenance and Release

## Build and Validate

Python 3.10+ is sufficient; no third-party Python packages are required.

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

Edit structured metadata in `data/`, then rebuild. The six inventory pages, dataset page, bibliography index, and homepage data bundle are generated. Other explanatory pages are maintained manually.

`homepage/index.html` opens directly from disk without a server. The static catalogue uses a generated local JavaScript data bundle, so it works without fetch access on file URLs.

## Before Public Release

- [x] Repository: https://github.com/loong8888/Limited-Observation-Human-Reconstruction .
- [ ] Confirm the author-finalized v2 PDF is the intended public release copy.
- [ ] Add the actual arXiv DOI/identifier once assigned. The template paper's identifier is not ours.
- [x] Previously unresolved metadata revisited against primary sources; see the audit and corrections log.
- [x] Original code MIT / original documentation CC BY 4.0 approved by the authors; manuscript and third-party assets excluded.
- [ ] Confirm rights to public release of the survey PDF and overview figure.
- [ ] Update the draft citation and remove the unpublished status only when appropriate.
- [ ] Confirm author affiliations and contact preferences.
- [ ] Review all third-party licenses separately before redistributing any data or weights.

The Git remote targets the repository above. GitHub Pages deployment is a separate optional step; the validation workflow does not publish a website.

## GitHub Pages

After publishing the repository, choose **Settings → Pages → Deploy from a branch**, select the main branch and root folder. Visit the resulting site at its `/homepage/` path. No build framework or package installation is required. Update README navigation with the assigned URL.

The validation workflow runs only repository-integrity checks; it does not publish the site.

## Update Policy

Keep manuscript-derived records distinguishable from later additions. In `data/provenance.json`, source hashes identify the imported snapshot, not all subsequent revisions. Record additions and corrections in `CHANGELOG.md`. Do not silently overwrite the historical snapshot claim.

The build checks resolve local paths and citation IDs, not remote URL availability or the scientific correctness of metadata.
