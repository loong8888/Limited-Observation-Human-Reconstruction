# Feature-Aligned Reconstruction
[Back to repository](../README.md) · Manuscript Section 4.2

Associate image evidence with 3D queries or primitives through projection, voxel features, stereo matching, or cross-view correspondence.

> Supervised completion is learned from training data. Hybrids such as ECON and SIFU also use mechanisms discussed in other families.

We summarize representative work reviewed in our survey below. PA = pixel alignment; VA = voxel alignment; SDS = score distillation. A dash indicates information not reported in the cited source.

| Method | Year | Input | Representation | Alignment | Mechanism | Source |
| --- | --- | --- | --- | --- | --- | --- |
| PIFu | 2019 | image | occupancy; texture/UV | PA | Pixel-aligned implicit function | [Reference](papers.md#saito2019pifu) · [Code](https://github.com/shunsukesaito/PIFu) |
| DeepHuman | 2019 | image | occupancy | VA | Volume-to-volume translation | [Reference](papers.md#deephuman2019) |
| PIFuHD | 2020 | image | occupancy | PA | Coarse-to-fine with normal maps | [Reference](papers.md#saito2020pifuhd) · [Code](https://github.com/facebookresearch/pifuhd) |
| Geo-PIFu | 2020 | image | occupancy | PA, VA | Latent voxel features | [Reference](papers.md#geopifu2020) |
| ARCH | 2020 | image | occupancy | PA | Canonical-space prediction | [Reference](papers.md#huang2020arch) |
| StereoPIFu | 2021 | stereo pair | occupancy | PA, VA | Stereo cost volume and relative depth | [Reference](papers.md#hong2021stereopifu) |
| NHP | 2021 | sparse-view video | NeRF | PA, body | Temporal and cross-view feature fusion | [Reference](papers.md#kwon2021nhp) |
| HEI-Human | 2021 | image | mesh; SDF | PA | Explicit-implicit hybrid | [Reference](papers.md#heihuman2024) |
| PaMIR | 2022 | image | occupancy | PA, VA | Voxelized SMPL condition | [Reference](papers.md#zheng2021pamir) |
| ICON | 2022 | image | SDF | PA | SMPL normal and distance cues | [Reference](papers.md#xiu2022icon) · [Code](https://github.com/YuliangXiu/ICON) |
| FOF | 2022 | image | occupancy | PA | Fourier occupancy field | [Reference](papers.md#feng2022fof) |
| DoubleField | 2022 | sparse views | occupancy; NeRF | PA | Surface-radiance coupling | [Reference](papers.md#shao2022doublefield) |
| KeypointNeRF | 2022 | sparse views | NeRF | PA | Keypoint-relative encoding | [Reference](papers.md#mihajlovic2022keypointnerf) |
| ECON | 2023 | image | mesh | PA | Normal integration, SMPL-X completion | [Reference](papers.md#xiu2023econ) · [Code](https://github.com/YuliangXiu/ECON) |
| D-IF | 2023 | image | occupancy | PA | Implicit distribution field | [Reference](papers.md#yang2023dif) |
| DIFu | 2023 | image | occupancy | PA, VA | Depth-guided voxel features | [Reference](papers.md#difu2023) |
| GTA | 2023 | image | mesh; texture/UV | PA | Transformer geometry-texture decoupling | [Reference](papers.md#chen2023gta) |
| 2K2K | 2023 | image | depth; mesh | PA | Part-wise high-resolution depth | [Reference](papers.md#han20232k2k) |
| TransHuman | 2023 | sparse views | NeRF | Body, image | Canonical encoding and part relationships | [Reference](papers.md#pan2023transhuman) |
| SHERF | 2023 | image | NeRF | Hierarchical | Global, point, and pixel features | [Reference](papers.md#hu2023sherf) |
| SIFU | 2024 | image | mesh; texture/UV | PA | Side-view decoupling, diffusion texture | [Reference](papers.md#zhang2024sifu) |
| ANIM | 2024 | image; depth | SDF | PA, VA | Pixel- and voxel-aligned features | [Reference](papers.md#anim2024) |
| GPS-Gaussian | 2024 | sparse views | 3D Gaussians | Pixel, depth | Stereo depth and pixel-wise GS maps | [Reference](papers.md#zheng2024gpsgaussian) |
| GHG | 2025 | sparse views | 3D Gaussians | UV | Multiple body-template scaffolds | [Reference](papers.md#kwon2024ghg) |
| RoGSplat | 2025 | sparse views | 3D Gaussians | PA, VA | Image-aligned prior points | [Reference](papers.md#xiao2025rogsplat) |
| HaP | 2025 | image | point cloud | Explicit | Points guided by depth and SMPL | [Reference](papers.md#tang2025hap) |
| GBC-Splat | 2025 | sparse views | 3D Gaussians | PA | Generalizable Gaussians | [Reference](papers.md#gbcsplat2025) |
