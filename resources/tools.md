# Models and Tools
[Back to repository](../README.md)

These are complementary implementation resources, not evaluated baselines. Official repository pages were accessed on 2026-11-13; installations, model weights, and runtime compatibility were not tested. Consult each project for current licenses.

## Body models

### [SMPL-X](https://github.com/vchoutas/smplx)

Parametric body, face, and hand modeling for structural scaffolds.

**Caution:** Code access and model-data access have separate terms; fitting a template does not recover clothing.

## Rendering and geometry

### [PyTorch3D](https://github.com/facebookresearch/pytorch3d)

Differentiable 3D components for geometry and rendering pipelines.

**Caution:** Provides components, not a complete occluded-human reconstruction system.

### [nvdiffrast](https://github.com/NVlabs/nvdiffrast)

Differentiable rasterization primitives for mesh-based pipelines.

**Caution:** Rasterization cannot infer unseen geometry by itself.

## Gaussian rendering

### [gsplat](https://github.com/nerfstudio-project/gsplat)

CUDA-accelerated Gaussian-splatting rasterization.

**Caution:** Human articulation, deformation, and completion require additional modeling.

## Camera estimation

### [COLMAP](https://github.com/colmap/colmap)

Structure-from-motion and multi-view stereo for suitable static evidence.

**Caution:** A moving articulated person violates a static-scene assumption; do not apply blindly.

## Geometry processing

### [Open3D](https://github.com/isl-org/Open3D)

Point-cloud and mesh processing, registration, and inspection.

**Caution:** Check alignment and visibility before using geometric comparisons.

## Evaluation

### [LPIPS](https://github.com/richzhang/PerceptualSimilarity)

Learned perceptual image-distance implementation.

**Caution:** Specify version, backbone, image scaling, crop, and whether LPIPS is multiplied by 1000.

## Generative priors

### [Diffusers](https://github.com/huggingface/diffusers)

Reusable diffusion-model components for image and video priors.

**Caution:** Models have separate licenses and may hallucinate identity-inconsistent detail.

## Related collections

### [Awesome Digital Human](https://github.com/weihaox/awesome-digital-human)

Broader digital-human modeling, generation, animation, and digitization resources.

**Caution:** Discovery collection; verify each entry against its original source.

### [Awesome 3D Human Reconstruction](https://github.com/rlczddl/awesome-3d-human-reconstruction)

Complementary human reconstruction literature collection.

**Caution:** A complementary index, not an independently controlled comparison.
