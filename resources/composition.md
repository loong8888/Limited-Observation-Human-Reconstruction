# Composition and Prior Interfaces
[Back to repository](../README.md)

A practical pipeline often uses several families. The six-family taxonomy is therefore complemented by component-level reasoning, rather than a seventh mutually exclusive family.

## Five Generative Interfaces

| Interface | Where the generator interacts | Questions to ask |
| --- | --- | --- |
| Image-space completion | Missing or unreliable image content | Are synthesized pixels distinguished from observations? |
| 3D / UV completion | Geometry, canonical features, or texture space | Are seams, pose consistency, and visibility accounted for? |
| Score distillation | Gradients derived from rendered views | Does guidance preserve measured content and identity? |
| Observation synthesis | Pseudo-views or pseudo-frames | Are generated views geometrically consistent? |
| Iterative loop | Alternating or coupled generation and 3D updates | How are errors propagated or corrected across iterations? |

## Recurring System Patterns

| Pattern | Pipeline | Examples discussed in the manuscript |
| --- | --- | --- |
| Scaffold plus completion | Structural estimate → free-form or generative completion | ECON, TeCH, OccFusion |
| Aggregate, then complete | Multi-frame fusion → unresolved-region completion | SOAR, AHOY |
| Synthesize, then reconstruct | Generated pseudo-observations → 3D recovery | SiTH, PSHuman |
| Reconstruct, then refine | Initial 3D estimate → appearance or geometry improvement | SIFU, Human-LRM |
| Distillation into shared models | Expensive priors or generated data → reusable inference | IDOL; Human-3Diffusion is a coupled-sampling boundary case |

These are analytical patterns, not literal execution graphs for every implementation. Consult the original paper before attributing an exact update order or optimization objective. Links and bibliographic records are in the [paper index](papers.md).
