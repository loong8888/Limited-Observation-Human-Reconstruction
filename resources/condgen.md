# Conditional Generation
[Back to repository](../README.md) · Manuscript Section 4.6

Generate human geometry or appearance from semantic, identity, or latent conditions; also provide priors to reconstruction pipelines.

> Conditional generation need not recover a particular observed subject. Body scaffolds and volumetric primitives do not automatically imply full clothed-surface recovery.

These rows reproduce the manuscript inventory. Years and technical labels are imported; see the [provenance policy](../data/README.md). PA = pixel alignment; VA = voxel alignment; SDS = score distillation. A dash means unreported or not specified by the source table.

## Text-driven score distillation

| Method | Year | Condition | Representation | Mechanism | Source |
| --- | --- | --- | --- | --- | --- |
| AvatarCLIP | 2022 | text | SDF; parametric body/shape | CLIP-guided optimization | [Reference](papers.md#hong2022avatarclip) |
| DreamHuman | 2023 | text | NeRF; parametric body/shape | SDS | [Reference](papers.md#kolotouros2023dreamhuman) |
| AvatarCraft | 2023 | text | implicit field/surface; parametric body/shape | SDS, shape control | [Reference](papers.md#jiang2023avatarcraft) |
| DreamWaltz | 2023 | text | NeRF; parametric body/shape | Skeleton-conditioned SDS | [Reference](papers.md#huang2023dreamwaltz) · [Code](https://github.com/IDEA-Research/DreamWaltz) |
| HeadSculpt | 2023 | text | head | Landmark-conditioned SDS | [Reference](papers.md#han2023headsculpt) |
| DreamAvatar | 2024 | text; parametric body/shape | NeRF; parametric body/shape | SMPL-guided SDS | [Reference](papers.md#cao2024dreamavatar) |
| TADA | 2024 | text | mesh; texture/UV; parametric body/shape | SDS | [Reference](papers.md#liao2024tada) |
| HumanNorm | 2024 | text | mesh | Normal and depth SDS | [Reference](papers.md#huang2024humannorm) |
| HeadArtist | 2024 | text | head | Self score distillation | [Reference](papers.md#liu2024headartist) |
| HeadStudio | 2025 | text | 3D Gaussians; head | SDS | [Reference](papers.md#zhou2024headstudio) |
| DreamWaltz-G | 2025 | text | 3D Gaussians; parametric body/shape | Skeleton-guided SDS | [Reference](papers.md#huang2024dreamwaltzg) |

## Related observation-synthesis pipeline

| Method | Year | Condition | Representation | Mechanism | Source |
| --- | --- | --- | --- | --- | --- |
| TGRHuman | 2026 | text | mesh; texture/UV | Diffusion renderer, UV inpainting | [Reference](papers.md#tgrhuman2026) |

## 3D generative models and image-to-3D lifting

| Method | Year | Condition | Representation | Mechanism | Source |
| --- | --- | --- | --- | --- | --- |
| gDNA | 2022 | latent code | implicit field/surface | Generative model of scans | [Reference](papers.md#chen2022gdna) |
| AvatarGen | 2023 | latent code | triplane; parametric body/shape | 3D-aware GAN | [Reference](papers.md#zhang2023avatargen) |
| EVA3D | 2023 | latent code | NeRF | 3D-aware GAN | [Reference](papers.md#hong2022eva3d) |
| PrimDiffusion | 2023 | noise | occupancy | 3D diffusion | [Reference](papers.md#chen2023primdiffusion) |
| StructLDM | 2025 | noise; edits | surface latent | Latent diffusion | [Reference](papers.md#hu2024structldm) |
| AvatarPopUp | 2025 | text; image | parametric body/shape; texture/UV | Image diffusion and 3D lifting | [Reference](papers.md#kolotouros2024avatarpopup) |
| GenLCA | 2026 | noise | codec avatar | 3D diffusion from videos | [Reference](papers.md#genlca2026) |

## Human image and video generation (no 3D state)

| Method | Year | Condition | Representation | Mechanism | Source |
| --- | --- | --- | --- | --- | --- |
| Animate Anyone | 2024 | image; pose | monocular video | Pose-guided video diffusion | [Reference](papers.md#hu2024animateanyone) |
| Champ | 2025 | image; parametric body/shape | monocular video | SMPL-guided video diffusion | [Reference](papers.md#zhu2024champ) |
| HumanGif | 2025 | image | image | View and pose synthesis | [Reference](papers.md#hu2025humangif) |
