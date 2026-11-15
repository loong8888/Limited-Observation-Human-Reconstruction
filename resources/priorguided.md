# Generative-Prior-Guided Optimization
[Back to repository](../README.md) · Manuscript Section 4.4

Couple subject-specific reconstruction to generative guidance through image completion, 3D/UV completion, score distillation, observation synthesis, or iterative loops.

> The inventory includes neighboring restoration methods. Guidance must remain anchored to valid evidence; photorealism alone does not establish identity fidelity.

These rows reproduce the manuscript inventory. Years and technical labels are imported; see the [provenance policy](../data/README.md). PA = pixel alignment; VA = voxel alignment; SDS = score distillation. A dash means unreported or not specified by the source table.

## Image-space completion and restoration

| Method | Year | Prior / mechanism | Input | Conditioning | Source |
| --- | --- | --- | --- | --- | --- |
| OccFusion | 2024 | Inpainting and SDS | occluded monocular video | current renders; mask; rendered body/face structure | [Reference](papers.md#sun2024occfusion) |
| BAGA | 2024 | Blur formation model | blurred monocular video; multi-view | - | [Reference](papers.md#niu2024baga) |
| Deblur-Avatar | 2025 | Human-motion blur model | blurred monocular video | - | [Reference](papers.md#luo2025debluravatar) |
| InpaintHuman | 2026 | Identity-preserving inpainting | occluded monocular video | image; mask | [Reference](papers.md#inpainthuman2026) |
| Deblur4DGS | 2026 | Exposure regularization | blurred monocular video | - | [Reference](papers.md#deblur4dgs2026) |
| AHOY | 2026 | Identity-finetuned diffusion | occluded monocular video | image; rendered body/face structure | [Reference](papers.md#mir2026ahoy) |

## Completion in 3D and UV space

| Method | Year | Prior / mechanism | Input | Conditioning | Source |
| --- | --- | --- | --- | --- | --- |
| ECON | 2023 | IF-Net shape completion | image | rendered body/face structure | [Reference](papers.md#xiu2023econ) · [Code](https://github.com/YuliangXiu/ECON) |
| InFusion | 2024 | Depth-guided Gaussian inpainting | occluded 3D Gaussians | current renders; mask | [Reference](papers.md#liu2024infusion) |
| TexDreamer | 2025 | UV texture diffusion | text; image | text; image | [Reference](papers.md#liu2024texdreamer) |
| MoGA | 2025 | 3D generative avatar inversion | image | image | [Reference](papers.md#dong2025moga) |
| DiGS-Avatar | 2026 | UV-latent diffusion completion | image | image | [Reference](papers.md#digsavatar2026) |

## Score distillation with observation-conditioned priors

| Method | Year | Prior / mechanism | Input | Conditioning | Source |
| --- | --- | --- | --- | --- | --- |
| TeCH | 2024 | Personalized SDS | image | text; image; rendered body/face structure | [Reference](papers.md#huang2024tech) · [Code](https://github.com/huangyangyi/TeCH) |
| PuzzleAvatar | 2024 | Asset tokens and SDS | photo album | text; image | [Reference](papers.md#xiu2024puzzleavatar) |
| SOAR | 2024 | SDS refinement of video avatar | monocular video | image | [Reference](papers.md#pan2024soar) · [Code](https://github.com/hangg7/soar) |
| GeneMAN | 2025 | Human-specific diffusion priors | image | text; image | [Reference](papers.md#gene2025man) |
| PFAvatar | 2026 | Pose-aware personalization | photo album | image; rendered body/face structure | [Reference](papers.md#pfavatar2026) |

## Multi-view and video diffusion as observation synthesis

| Method | Year | Prior / mechanism | Input | Conditioning | Source |
| --- | --- | --- | --- | --- | --- |
| SiTH | 2024 | Back-view hallucination | image | image; rendered body/face structure | [Reference](papers.md#ho2024sith) |
| Morphable Diff. | 2024 | Morphable-mesh conditioning | image | image; rendered body/face structure | [Reference](papers.md#chen2024morphable) |
| Human4DiT | 2024 | Orbit video diffusion | image | image; rendered body/face structure | [Reference](papers.md#shao2024human4dit) |
| MagicMan | 2025 | Dense multi-view diffusion | image | image; rendered body/face structure | [Reference](papers.md#he2024magicman) |
| PSHuman | 2025 | Normal and color diffusion | image | image; rendered body/face structure | [Reference](papers.md#li2024pshuman) |
| Pippo | 2025 | Multi-view diffusion transformer | image | image | [Reference](papers.md#kant2025pippo) |
| CAP4D | 2025 | Morphable multi-view diffusion | 1-100 image | image; rendered body/face structure | [Reference](papers.md#taubner2025cap4d) |
| GAF | 2025 | Multi-view head diffusion | monocular video | image; rendered body/face structure | [Reference](papers.md#tang2025gaf) |
| CHROME | 2025 | Occlusion-free view synthesis | occluded image | image | [Reference](papers.md#arindam2025chrome) |
| AniGS | 2025 | Canonical multi-view synthesis | image | image; rendered body/face structure | [Reference](papers.md#qiu2025anigs) |
| SinGS | 2025 | Kinematic human diffusion | image | image; rendered body/face structure | [Reference](papers.md#singh2025sings) |
| GAS | 2025 | Video diffusion on NeRF renders | image | image; rendered body/face structure | [Reference](papers.md#gas2025) |
| MVP4D | 2025 | Multi-view video diffusion | image | image | [Reference](papers.md#taubner2025mvp4d) |
| UP2You | 2026 | Photo rectification | photo album | image | [Reference](papers.md#cai2025up2you) |
| PRISM | 2027 | Multi-source prior distillation | image | image; rendered body/face structure | [Reference](papers.md#prism2026) |

## Iterative reconstruction-generation loops

| Method | Year | Prior / mechanism | Input | Conditioning | Source |
| --- | --- | --- | --- | --- | --- |
| NeRFiller | 2024 | Iterative dataset update | occluded scene | current renders; mask | [Reference](papers.md#weber2024nerfiller) |
| Human-3Diffusion | 2024 | Per-step 3DGS projection | image | image; current renders | [Reference](papers.md#xue2024human3diffusion) |
| Gen-3Diffusion | 2024 | 2D-3D diffusion synergy | image | image; current renders | [Reference](papers.md#xue2024gen3diffusion) |
| AdaHuman | 2025 | Joint diffusion, part-aware refinement | image | image; rendered body/face structure; current renders | [Reference](papers.md#huang2025adahuman) |
