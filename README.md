<h1 align="center">Limited-Observation Human Reconstruction</h1>
<p align="center"><strong>From incomplete evidence to complete 3D humans.</strong></p>
<p align="center">A companion resource for<br><em>Reconstructing Complete 3D Humans from Limited Observations: A Survey</em></p>
<p align="center"><a href="paper/survey-draft.pdf">Survey</a> &middot; <a href="resources/taxonomy.md">Taxonomy</a> &middot; <a href="resources/papers.md">Paper index</a> &middot; <a href="data/references.bib">BibTeX</a> &middot; <a href="CONTRIBUTING.md">Contribute</a></p>

<p align="center"><img src="assets/survey-overview.png" width="900" alt="Survey overview: six reconstruction and generation families, their composition, datasets, evaluation, and research directions"></p>

**Jinlong Fan · Jing Zhang · Mingming Gong · Yuxiang Yang**

How can we reconstruct a complete 3D human when the available observations reveal only part of the person? A single photograph leaves the back unseen; an occluded video may never expose a hidden limb; and a personal photo collection may span different poses, outfits, cameras, and years. Recovering geometry, appearance, and deformation from such evidence requires more than fitting what is visible: it requires deciding how observations and prior knowledge should work together.

In our survey, **Reconstructing Complete 3D Humans from Limited Observations**, we organize this problem by separating **what evidence is missing** from **how methods compensate for it**. We characterize limited observation along four axes and review six mechanism-based method families, connecting template fitting and feature alignment with temporal aggregation, generative guidance, feed-forward reconstruction, and conditional generation. Our emphasis is on the interaction between reconstruction and generation: preserving subject-specific evidence while inferring plausible content that was not observed. Full-body reconstruction is our main focus, with head and hand methods included where they illuminate shared mechanisms.

We maintain this repository as a companion to the survey and a practical entry point into the field. Alongside the literature organized by our taxonomy, we collect datasets, official implementations, reusable tools, reading routes, and evaluation considerations. These resources help readers compare assumptions, identify suitable starting points, and distinguish fidelity to observed evidence from the plausibility of completed regions. We welcome contributions that extend the collection and clarify the connections between methods.

**Repository:** [loong8888/Limited-Observation-Human-Reconstruction](https://github.com/loong8888/Limited-Observation-Human-Reconstruction)

## Search the Literature

**[Open the searchable literature catalogue](https://loong8888.github.io/Limited-Observation-Human-Reconstruction/homepage/)**

Search papers by title, author, method, input, or representation; filter by method family and year, explore datasets and tools, and copy BibTeX citations. Click the preview below to start searching.

<a href="https://loong8888.github.io/Limited-Observation-Human-Reconstruction/homepage/">
  <img src="assets/literature-search-preview.png" width="960" alt="Search our literature catalogue: search field, method-family and year filters, and results for occlusion-related papers">
</a>

## Start Here

<p><img src="assets/scan-face.svg" width="22" alt=""> <strong>Read the evidence. Trace the prior. Inspect the completion.</strong></p>

| Explore the literature | Build and evaluate |
| :--- | :--- |
| [Six method families](resources/taxonomy.md) | [Datasets and capture resources](resources/datasets.md) |
| [All 243 bibliography records](resources/papers.md) | [Models, rendering, and geometry tools](resources/tools.md) |
| [Reading routes by observation regime](resources/reading-routes.md) | [Evaluation and reproducibility checklist](resources/evaluation.md) |
| [Official implementation entry points](resources/implementations.md) | [Structured catalogue data](data/README.md) |
| [Hybrid systems and prior interfaces](resources/composition.md) | [Open problems and research opportunities](resources/research-directions.md) |



## Four Observation Axes

| Axis | Rich evidence | Limited evidence |
| :--- | :--- | :--- |
| Spatial completeness | Dense calibrated views | Sparse views, a single image, a truncated crop |
| Temporal completeness | Diverse motion sequences | Short clips or a single pose |
| Observation quality | Clean, visible observations | Occlusion, blur, noise, archival damage |
| Observation coherence | Synchronized, consistent capture | Photos spanning cameras, time, outfits, and appearance |

The axes may interact. Text-only generation is a useful boundary case, not evidence of a captured subject.

## Six Method Families

<table><tr><td align="center"><a href="resources/template.md"><img src="assets/user.svg" width="38" alt=""><br>Template fitting</a></td><td align="center"><a href="resources/feature.md"><img src="assets/scan-face.svg" width="38" alt=""><br>Feature alignment</a></td><td align="center"><a href="resources/temporal.md"><img src="assets/layers.svg" width="38" alt=""><br>Temporal aggregation</a></td></tr><tr><td align="center"><a href="resources/priorguided.md"><img src="assets/wand-2.svg" width="38" alt=""><br>Prior-guided</a></td><td align="center"><a href="resources/feedforward.md"><img src="assets/cpu.svg" width="38" alt=""><br>Feed-forward</a></td><td align="center"><a href="resources/condgen.md"><img src="assets/sparkles.svg" width="38" alt=""><br>Conditional generation</a></td></tr></table>

| Family | Main compensatory mechanism | Inventory |
| :--- | :--- | :--- |
| 4.1 Template-constrained fitting | Restrict the hypothesis space with a body, pose, or motion model | [36 entries](resources/template.md) |
| 4.2 Feature-aligned reconstruction | Associate image evidence with 3D queries or primitives | [27 entries](resources/feature.md) |
| 4.3 Canonical-space temporal aggregation | Register and fuse observations in a shared space | [19 entries](resources/temporal.md) |
| 4.4 Generative-prior-guided optimization | Couple a subject-specific state to generative guidance | [35 entries](resources/priorguided.md) |
| 4.5 Feed-forward generative reconstruction | Predict or sample from a shared learned model | [15 entries](resources/feedforward.md) |
| 4.6 Conditional generation | Generate humans from semantic, identity, or latent conditions | [22 entries](resources/condgen.md) |

Inventories follow the manuscript tables, including explicitly discussed neighboring methods. They are **not mutually exclusive memberships**, and the evidence-to-prior ordering is conceptual rather than a measured ranking.

## What We Cover

Our collection currently includes **243 references**, **154 method-inventory entries**, and **26 dataset entries**. We connect these records to paper sources and to project pages and code where available. We also provide complementary tools and reading routes beyond the survey's core method discussion.

We organize methods by their compensatory mechanisms rather than by representation alone. The same paper may therefore contribute to several families, and inclusion does not imply that its input assumptions or outputs are interchangeable with those of neighboring methods. Likewise, results reported under different capture settings, splits, masks, or training budgets should not be read as a controlled leaderboard. Our [evaluation guide](resources/evaluation.md) explains the distinctions that matter when comparing systems.

## Repository Map

```text
assets/       Survey overview and navigation icons
data/         Paper metadata, method/dataset inventories, BibTeX, tool links
homepage/     Searchable static catalogue, works without a build server
paper/        Survey manuscript and BibTeX citation
resources/    Six families, datasets, evaluation, reading routes, tools
scripts/      Rebuild catalogue pages and validate repository consistency
.github/      Issue templates and catalogue validation
```

## Cite and Contribute

If our survey or this collection supports your research, please cite [our survey](paper/citation.bib). For specific methods, datasets, or software, please also cite the corresponding original work.

Corrections, new resources, and discussion of boundary cases are welcome. Please provide an official source, the relevant mechanism, and any evaluation caveats. See [CONTRIBUTING.md](CONTRIBUTING.md).

**Main Contact:** [Jinlong Fan](mailto:jfan@hdu.edu.cn), [Yuxiang Yang](mailto:yyx@hdu.edu.cn), Hangzhou Dianzi University.

## Acknowledgments and Rights

We thank [Human-Centric AI Resources](https://github.com/cseeyangchen/Human-Centric-AI) for inspiring the organization of this collection. We also recommend [Awesome Digital Human](https://github.com/weihaox/awesome-digital-human) and [Awesome 3D Human Reconstruction](https://github.com/rlczddl/awesome-3d-human-reconstruction) as complementary resources.

Our original scripts are MIT-licensed, and our original resource documentation is licensed under CC BY 4.0. The manuscript, figures, and third-party papers, datasets, models, code, and icons retain their respective rights and terms. See [LICENSE](LICENSE) for details.
