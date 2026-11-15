# Feed-Forward Generative Reconstruction
[Back to repository](../README.md) · Manuscript Section 4.5

Predict or sample subject-specific humans using shared learned models without per-subject parameter optimization.

> Sampling can require repeated network evaluations. Fast prediction, complete geometry, calibrated uncertainty, and native animatability are different properties.

These rows reproduce the manuscript inventory. Years and technical labels are imported; see the [provenance policy](../data/README.md). PA = pixel alignment; VA = voxel alignment; SDS = score distillation. A dash means unreported or not specified by the source table.

## Full body

| Method | Year | Input | Representation | Animatable | Mechanism | Source |
| --- | --- | --- | --- | --- | --- | --- |
| SHERF | 2023 | image | NeRF | yes | Canonical-space feature encoding | [Reference](papers.md#hu2023sherf) |
| Human-LRM | 2024 | image | triplane | no | Initial triplane, novel-view diffusion, reconstruction | [Reference](papers.md#weng2024humanlrm) |
| HumanSplat | 2024 | image | 3D Gaussians | no | Multi-view diffusion latents, structure priors | [Reference](papers.md#pan2024humansplat) |
| MHCDiff | 2024 | occluded image | point cloud | no | Point diffusion conditioned on body hypotheses | [Reference](papers.md#kim2024mhcdiff) |
| Human-3Diffusion | 2024 | image | 3D Gaussians | - | Repeated 3D reconstruction inside diffusion sampling | [Reference](papers.md#xue2024human3diffusion) |
| IDOL | 2025 | image | 3D Gaussians | yes | Synthetic HuGe100K corpus | [Reference](papers.md#zhuang2025idol) |
| LHM | 2025 | image | 3D Gaussians | yes | Body-structure and image tokens | [Reference](papers.md#qiu2025lhm) · [Code](https://github.com/aigc3d/LHM) |
| PF-LHM | 2025 | 1-N image | 3D Gaussians | yes | Pose-free multi-image input | [Reference](papers.md#qiu2025pflhm) |
| HumanRAM | 2025 | 1-N image | neural rendering | yes | SMPL-X neural texture, pose conditions | [Reference](papers.md#yu2025humanram) |
| SIGMAN | 2025 | image | 3D Gaussians | - | Latent diffusion over UV Gaussians | [Reference](papers.md#yang2025sigman) |
| HART | 2025 | sparse views | mesh; 3D Gaussians | yes | Human-aligned mesh and SMPL-X | [Reference](papers.md#chen2025hart) |
| Human3R | 2026 | monocular video | parametric body/shape; scene | yes | Prompt-tuned CUT3R | [Reference](papers.md#human3r2025) |

## Heads

| Method | Year | Input | Representation | Animatable | Mechanism | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Portrait4D | 2024 | image | triplane | yes | Synthetic 4D head data | [Reference](papers.md#deng2024portrait4d) |
| Avat3r | 2025 | sparse views | 3D Gaussians | yes | DUSt3R and Sapiens features | [Reference](papers.md#kirschstein2025avat3r) |
| FlexAvatar | 2026 | 1-N image | 3D Gaussians | yes | Head query tokens, no pose labels | [Reference](papers.md#flexavatar2026) |
