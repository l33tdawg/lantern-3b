# Licensing

This repository mixes two kinds of material.

- Guard and evaluation code in `guard/` and `evaluation/` is Apache-2.0. See `LICENSE`.
- The model adapters, model card and model evaluation results are a derivative of Qwen2.5-VL-3B-Instruct and are distributed under the Qwen Research License. See `LICENSE-QWEN-RESEARCH`.
- The base Qwen2.5-VL-3B-Instruct weights are not included. Obtain them separately under their license.

The Qwen Research License permits non-commercial use, reproduction, distribution and derivative works only. Commercial use requires a license from Alibaba Cloud. Redistribution of the adapters must include `LICENSE-QWEN-RESEARCH` and `NOTICE.md`.

The guard is a canonicalization and authorization boundary for specific save and recall actions. It is not a general safety filter, and it does not relicense anything.

