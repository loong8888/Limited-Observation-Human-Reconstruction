# Taxonomy: Missing Evidence and Compensatory Mechanisms
[Back to repository](../README.md)

## Two Independent Questions

**What is missing?** Describe spatial completeness, temporal completeness, observation quality, and observation coherence. Input modality alone is insufficient: a clean single photograph and an occluded single photograph do not present the same inference problem.

**How is it compensated?** Identify the mechanism that narrows, extends, or samples the set of plausible complete humans.

| Family | Mechanism | What it can establish | Important limit |
| --- | --- | --- | --- |
| [Template fitting](template.md) | Model manifold and structural priors | Articulated body scaffold | Clothing and hair exceed standard body-model capacity |
| [Feature alignment](feature.md) | Evidence-to-3D feature correspondence | Image-conditioned geometry or appearance | Unseen content inherits training bias |
| [Temporal aggregation](temporal.md) | Canonical registration and fusion | Accumulated subject-specific evidence | Never-observed regions remain ambiguous |
| [Prior-guided optimization](priorguided.md) | External generative guidance | Completion compatible with selected priors | Guidance may drift from identity or observed detail |
| [Feed-forward reconstruction](feedforward.md) | Shared learned reconstruction or sampling | Efficient conditional inference | Generalization and calibration remain concerns |
| [Conditional generation](condgen.md) | Semantic, identity, or latent conditioning | Controllable human generation | Fidelity to a particular captured subject is not implied |

## Classification Rules

1. Classify the compensatory mechanism, not merely the output representation. A Gaussian representation can appear in several families.
2. A feed-forward body-parameter regressor remains template-constrained; inference speed alone does not make it a generative reconstruction model.
3. Keep **native capability**, **optional refinement**, and **a component supplied to another system** distinct.
4. Treat hybrids as combinations. A dominant-family tag is a reading aid, not a claim that other mechanisms are absent.
5. Preserve boundary-case notes from the manuscript. Section placement is not proof of exclusive membership.

The [composition guide](composition.md) connects the families. The [reading routes](reading-routes.md) instead start from the observations a reader actually has.
