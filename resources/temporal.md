# Canonical-Space Temporal Aggregation
[Back to repository](../README.md) · Manuscript Section 4.3

Register observations to a pose-neutral domain and accumulate reliable evidence over time.

> Transient occlusion can be resolved by other frames; permanently unseen content needs additional assumptions. MonoNHR is a single-image structural counterpart, not temporal aggregation.

We summarize representative work reviewed in our survey below. PA = pixel alignment; VA = voxel alignment; SDS = score distillation. A dash indicates information not reported in the cited source.

| Method | Year | Input | Representation | Completion / occlusion mechanism | Source |
| --- | --- | --- | --- | --- | --- |
| Neural Body | 2021 | sparse-view video | NeRF | - | [Reference](papers.md#peng2021neuralbody) · [Code](https://github.com/zju3dv/neuralbody) |
| HumanNeRF | 2022 | monocular video | NeRF | - | [Reference](papers.md#weng2022humannerf) · [Code](https://github.com/chungyiweng/humannerf) |
| ARAH | 2022 | sparse-view video | SDF | - | [Reference](papers.md#wang2022arah) |
| SelfRecon | 2022 | monocular video | SDF; mesh | - | [Reference](papers.md#jiang2022selfrecon) |
| MonoNHR | 2022 | image | mesh; NeRF | Symmetry-based mesh inpainting | [Reference](papers.md#mononhr2023) |
| Vid2Avatar | 2023 | monocular video | SDF | Self-supervised scene decomposition | [Reference](papers.md#guo2023vid2avatar) |
| InstantAvatar | 2023 | monocular video | NeRF | - | [Reference](papers.md#jiang2023instantavatar) |
| OccNeRF | 2023 | occluded monocular video | NeRF | Visibility, rendering-order priors | [Reference](papers.md#xiang2023occnerf) |
| 3DGS-Avatar | 2024 | monocular video | 3D Gaussians | - | [Reference](papers.md#qian2024gsavatar) |
| GaussianAvatar | 2024 | monocular video | 3D Gaussians | Pose-dependent deformation | [Reference](papers.md#hu2024gaussianavatar) |
| GauHuman | 2024 | monocular video | 3D Gaussians | - | [Reference](papers.md#hu2024gauhuman) |
| GART | 2024 | monocular video | 3D Gaussians | - | [Reference](papers.md#lei2024gart) |
| HINT | 2024 | sparse views | NeRF | Sagittal symmetry prior | [Reference](papers.md#hint2024) |
| Wild2Avatar | 2025 | occluded monocular video | NeRF | Occluder, human, background layers | [Reference](papers.md#xiang2024wild2avatar) |
| OccGaussian | 2025 | occluded monocular video | 3D Gaussians | Occlusion-aware feature aggregation | [Reference](papers.md#ye2025occgaussian) |
| SymGaussian | 2025 | occluded monocular video | 3D Gaussians | Multi-scale symmetry features | [Reference](papers.md#jiang2025symgaussian) |
| Vid2Avatar-Pro | 2025 | monocular video | 3D Gaussians | Universal prior from capture data | [Reference](papers.md#guo2025vid2avatarpro) |
| STG-Avatar | 2025 | monocular video | 3D Gaussians | - | [Reference](papers.md#jiang2025stgavatar) |
| U-4DGS | 2026 | occluded monocular video | 3D Gaussians | Per-Gaussian uncertainty | [Reference](papers.md#u4dgs2026) |
