# Datasets and Capture Resources
[Back to repository](../README.md) · Manuscript Section 5.1

Separate dataset content, input restriction, and reference fidelity before selecting an evaluation protocol.

> Sp / Te / Qu / Co indicate spatial, temporal, quality, and coherence axes. Parentheses denote imposed restrictions. Counts have different units; fitted bodies and generated images are not ground-truth clothed geometry.

These rows reproduce the manuscript inventory. Years and technical labels are imported; see the [provenance policy](../data/README.md). PA = pixel alignment; VA = voxel alignment; SDS = score distillation. A dash means unreported or not specified by the source table.

| Dataset | Type | Scale | Use | Axes | Reference | Source |
| --- | --- | --- | --- | --- | --- | --- |
| THuman2.0/ 2.1 | scan; (real capture) | about 500 scans (2.0) | Training | (Sp) | Textured scans | [Reference](papers.md#yu2021function4d) |
| THuman3.0 | scan; (real capture) | 20 human-garment combinations | Garment variation | (Sp) | Textured scans | [Reference](papers.md#su2023thuman3) |
| 2K2K | scan; (real capture) | 2,050 scans | High-resolution training | (Sp) | Textured scans | [Reference](papers.md#han20232k2k) |
| CustomHumans | scan; (real capture) | See cited release | Training | (Sp) | Textured scans | [Reference](papers.md#ho2023customhumans) |
| ZJU-MoCap | multi-view video; (real capture) | about 10 subjects | Aggregation, occlusion | (Sp, Qu) | Body fits; held-out views | [Reference](papers.md#peng2021neuralbody) · [Code](https://github.com/zju3dv/neuralbody) |
| ActorsHQ | dense multi-view video; (real capture) | 8 actors | High-fidelity reference | (Sp, Te) | Held-out views | [Reference](papers.md#isik2023humanrf) |
| DNA-Rendering | dense multi-view video; (real capture) | about 500 actors | 4D prior training | (Sp, Te) | Body fits; held-out views | [Reference](papers.md#cheng2023dnarendering) |
| MVHumanNet | multi-view video; (real capture) | 4,500 identities | Scaling 4D priors | (Sp, Te) | Body fits; held-out views | [Reference](papers.md#xiong2024mvhumannet) |
| HuMMan | image; depth; temporal/4D; (real capture) | 1,000 subjects | Multi-sensor training | (Sp, Te) | Depth, body fits | [Reference](papers.md#cai2022humman) |
| 4D-DRESS | scan; temporal/4D; (real capture) | 64 outfits | Cloth dynamics | (Te) | Clothed meshes | [Reference](papers.md#wang2024fourddress) |
| 3DPW | in-the-wild; monocular video; (real capture) | 60 sequences | Pose under occlusion | Qu | Body pose and shape | [Reference](papers.md#vonmarcard20183dpw) |
| EMDB | in-the-wild; monocular video; (real capture) | 10 subjects | Global body and camera | Te | Body, camera motion | [Reference](papers.md#kaufmann2023emdb) |
| WildAvatar | in-the-wild; monocular video; (real capture) | over 10,000 subjects | In-the-wild avatars | (Sp, Te) | Estimated SMPL | [Reference](papers.md#huang2025wildavatar) |
| BEDLAM | monocular video; (synthetic) | 271 bodies | Pose pretraining | (Sp, Te) | Synthetic meshes, pose | [Reference](papers.md#black2023bedlam) |
| SynBody | image; (synthetic) | 10,000 bodies | Perception pretraining | (Sp) | Synthetic meshes, pose | [Reference](papers.md#yang2023synbody) |
| HuGe100K | multi-view; image; (synthetic) | 100K subjects | Feed-forward training | (Sp) | Generated images only | [Reference](papers.md#zhuang2025idol) |
| RenderPeople | Commercial scans | Catalog-dependent | Training | (Sp) | Textured meshes | Not cited in source table |
| People-Snapshot | monocular video; (real capture) | See cited release | Avatar recovery | Te | Fits and images | [Reference](papers.md#alldieck2018peoplesnapshot) |
| CAPE | scan; temporal/4D; (real capture) | 15 subjects | Pose-dependent clothing | (Sp, Te) | Clothed meshes | [Reference](papers.md#ma2020cape) |
| AIST++ | multi-view video; pose; (real capture) | 30 subjects | Motion and rendering | (Sp, Te) | Pose, cameras | [Reference](papers.md#li2021aist) |
| Hi4D | interaction; multi-view; (real capture) | 20 pairs | Inter-person occlusion | Qu | Per-person meshes | [Reference](papers.md#yin2023hi4d) |
| BEHAVE | multi-view; depth; (real capture) | 8 subjects | Human-object contact | Qu | Body and object fits | [Reference](papers.md#bhatnagar2022behave) |
| RICH | monocular video; scan; scene; (real capture) | 22 subjects | Human-scene contact | Qu | SMPL-X and scene | [Reference](papers.md#huang2022rich) |
| PuzzleIOI | photo album; (real capture) | 41 identities, nearly 1K outfits | Album reconstruction | Sp, Co | A-posed scans | [Reference](papers.md#xiu2024puzzleavatar) |
| Harmony4D | interaction; monocular video; (real capture) | See cited release | Close interactions | Qu | Motion annotations | [Reference](papers.md#harmony4d2024) |
| OcMotion | occluded monocular video; (real capture) | 43 sequences | Occlusion robustness | Qu | Body annotations; no hidden RGB | [Reference](papers.md#huang2022ocmotion) |
