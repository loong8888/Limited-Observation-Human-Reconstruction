# Evaluation and Reproducibility
[Back to repository](../README.md)

**There is no cross-paper leaderboard here.** A better rendering score under one paper's split, mask, and training budget need not imply better completion under another's.

## Separate the Questions

| Target | Suitable evidence | What the result does not establish |
| --- | --- | --- |
| Observed-region fidelity | Visible RGB, silhouettes, landmarks | Quality of the unseen back |
| Held-out appearance | Calibrated held-out cameras | Exact surface geometry |
| Hidden-region geometry | Scans withheld from the input | Photorealistic texture |
| Animation | Unseen poses and temporal sequences | Identity preservation under all motion |
| Ambiguity | Multiple outputs and calibration/coverage tests | Calibration from diversity alone |

OcMotion visible-region rendering scores do not evaluate hidden appearance. ZJU-MoCap protocols with inserted occluders can preserve an unobstructed reference, but synthetic masks do not reproduce all physical occlusion effects. Dataset entries and source papers are in [datasets.md](datasets.md).

## Minimum Protocol Record

- Dataset release, subject IDs, train/test split, and permitted training assets.
- Camera calibration, input-view count, synchronization, and pose diversity.
- Visibility mask construction, persistent versus transient occlusion, and degraded-input parameters.
- Reference type: image, fitted body, scan, or generated supervision.
- Metric implementation, image resolution, background treatment, crop, and LPIPS scaling.
- Optimization steps, wall-clock time, hardware, seeds, and initialization.
- Pose/body-model fitting, segmentation, and external generative priors.
- Per-subject outcomes and variability, not only the best qualitative examples.
- Whether additional generated views are counted as evidence or prior-derived content.

## Region-Aware Reporting

Report observed, temporarily hidden, and never-observed regions separately when reference data permits. Record how visibility is computed. When hidden-region truth is unavailable, state that limitation instead of interpreting visible-pixel accuracy as completion accuracy.

For multiple plausible outputs, distinguish best-of-N performance from expected performance and report N and sampling cost. A posterior interpretation requires more than visual diversity.

## Practical Tools

[LPIPS](https://github.com/richzhang/PerceptualSimilarity) supports perceptual image comparison; [Open3D](https://github.com/isl-org/Open3D) provides geometric processing primitives. Neither makes experiments comparable automatically. See [tools.md](tools.md) for scope and licensing cautions.
