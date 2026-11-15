# Template-Constrained Fitting
[Back to repository](../README.md) · Manuscript Section 4.1

Restrict the human state to a statistical body-model manifold. Optimization, regression, and language-conditioned recovery can share this scaffold.

> Complete articulation does not imply complete clothed geometry. This inventory also includes neighboring scene, garment, and RGB-D estimation systems.

We summarize representative work reviewed in our survey below. PA = pixel alignment; VA = voxel alignment; SDS = score distillation. A dash indicates information not reported in the cited source.

## Body recovery from RGB

| Method | Year | Inference | Evidence | Prior | Occlusion / limitation handling | Source |
| --- | --- | --- | --- | --- | --- | --- |
| SMPLify | 2016 | optimization | keypoints | GMM pose | - | [Reference](papers.md#bogo2016smplify) |
| HMR | 2018 | regression | image | Adversarial | - | [Reference](papers.md#kanazawa2018hmr) |
| SMPLify-X | 2019 | optimization | keypoints; parametric body/shape; hand; head | VAE pose (VPoser) | - | [Reference](papers.md#pavlakos2019smplx) · [Code](https://github.com/vchoutas/smplx) |
| SPIN | 2019 | regression; optimization | image; keypoints | GMM pose | - | [Reference](papers.md#kolotouros2019spin) |
| PARE | 2021 | regression | image | Learned | Part attention | [Reference](papers.md#kocabas2021pare) |
| ProHMR | 2021 | regression | image | Normalizing flow | Pose distribution | [Reference](papers.md#kolotouros2021prohmr) |
| HuMoR | 2021 | optimization | monocular video; keypoints | CVAE motion | Temporal in-filling | [Reference](papers.md#rempe2021humor) |
| CLIFF | 2022 | regression | image; bounding box | Learned | Full-frame location | [Reference](papers.md#li2022cliff) |
| Pose-NDF | 2022 | prior | - | Neural distance field | Manifold projection | [Reference](papers.md#tiwari2022posendf) |
| VisDB | 2022 | regression; optimization | image | Learned | Visibility prediction | [Reference](papers.md#visdb2024) |
| HMR 2.0 | 2023 | regression | image | Data scale | - | [Reference](papers.md#goel2023hmr2) |
| ScoreHMR | 2024 | sampling | image; keypoints | Pose diffusion | Posterior sampling | [Reference](papers.md#stathopoulos2024scorehmr) |
| HaMeR | 2024 | regression | image; hand | Data scale | Truncation robustness | [Reference](papers.md#pavlakos2024hamer) |
| GenHMR | 2025 | sampling | image | Pose tokens | Generative uncertainty | [Reference](papers.md#saleem2025genhmr) |
| DPoser-X | 2025 | prior | - | Pose diffusion | Whole-body prior | [Reference](papers.md#lu2025dposerx) |
| PostoMETRO | 2025 | regression | image | VQ-VAE pose tokens | Pose tokens | [Reference](papers.md#yang2025postometro) |
| Wehrbein et al. | 2025 | regression | image | Normalizing flow | Heatmap supervision | [Reference](papers.md#wehrbein2025uncertainty) |

## Joint human, scene, and camera estimation

| Method | Year | Inference | Evidence | Prior | Occlusion / limitation handling | Source |
| --- | --- | --- | --- | --- | --- | --- |
| SLAHMR | 2023 | optimization | monocular video; camera trajectory | Motion prior | Motion in-filling | [Reference](papers.md#ye2023slahmr) |
| WHAM | 2024 | regression | monocular video | Motion encoder | Foot contact | [Reference](papers.md#shin2024wham) |
| TRAM | 2025 | regression; camera trajectory | monocular video | Video transformer | Human-robust SLAM | [Reference](papers.md#wang2024tram) |
| HSR | 2025 | optimization | monocular video | SMPL, implicit surfaces | Joint human-scene rendering | [Reference](papers.md#xue2024hsr) |
| HSfM | 2025 | optimization | sparse views | SMPL-X, scene prior | Multi-view alignment | [Reference](papers.md#muller2025hsfm) |
| ODHSR | 2025 | optimization | monocular video | SMPL, GS | Occlusion-aware silhouettes | [Reference](papers.md#odhsr2025) |
| JOSH | 2026 | optimization | monocular video | Scene, HMR initialization | Contact constraints | [Reference](papers.md#liu2026josh) |
| Human3R | 2026 | regression | monocular video | 4D foundation model | Visual prompt tuning | [Reference](papers.md#human3r2025) |
| GUSH3R | 2026 | regression | monocular video | Feed-forward GS | Human-scene Gaussians | [Reference](papers.md#abe2026gush3r) |

## Depth input

| Method | Year | Inference | Evidence | Prior | Occlusion / limitation handling | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Bogo et al. | 2015 | optimization | image; depth | Multi-resolution model | Coarse-to-fine alignment | [Reference](papers.md#bogo2015detailed) |
| DoubleFusion | 2018 | optimization | image; depth | SMPL | Embedded deformation | [Reference](papers.md#doublefusion2018) |
| POP | 2019 | optimization | image; depth | Body model | Full model from partial view | [Reference](papers.md#marin2019pop) |
| Dang et al. | 2023 | optimization | image; depth | Free space, shadow volume | Volumetric constraints | [Reference](papers.md#dang2023reconstructing) |
| PIFU-RGBD | 2023 | regression | image; depth | Implicit function | Depth point cloud | [Reference](papers.md#pifu-rgbd2023) |
| ANIM | 2024 | regression | image; depth | Implicit function | Depth-based geometry | [Reference](papers.md#anim2024) |
| Zhu et al. | 2025 | regression | image; depth | Parametric refinement | Front-back silhouette loss | [Reference](papers.md#finer2025rgbd) |

## Language-model priors

| Method | Year | Inference | Evidence | Prior | Occlusion / limitation handling | Source |
| --- | --- | --- | --- | --- | --- | --- |
| ChatPose | 2024 | regression | image; text | MLLM | Reasoning about pose | [Reference](papers.md#feng2024chatpose) |
| PromptHMR | 2025 | regression | image; text; bounding box | Promptable model | Spatial and text prompts | [Reference](papers.md#promptHMR2025) |
| ChatGarment | 2025 | regression | image; text | MLLM | Sewing patterns | [Reference](papers.md#chatgarment2025) |
