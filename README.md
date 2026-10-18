# Lantern 3B V81

A small English model for a computer that fits in your hand.

Lantern is the first device built on SAGE Commons: an offline-first assistant for people and places where the network is thin, expensive, or simply absent. V81 is the research preview of the language model inside it.

The model is a 3B fine-tune of Qwen2.5-VL-3B-Instruct, distributed as an ordered LoRA chain. It is small on purpose. A Lantern runs on a battery, on a desk, in a room with no data centre behind it. That constraint shapes the data, the answer length, and the decision to put a guard around memory and tool actions.

V81 is not a general assistant. It is a focused English model for short conversation, label and schedule questions, correction continuity, and guarded memory actions. The [model card](MODEL_CARD.md) is honest about where it still fails.

## What the numbers say

The evaluation separates the raw model from the guarded runtime. The guard is not decoration. It builds a save or recall from the trusted request, uses a supplied recall query even when the model asks for one, and repairs a failed-lookup answer that would otherwise claim absence.

| Panel | Raw V81 | Guarded V81 |
|---|---:|---:|
| Fresh 64-case sealed set | 64/64 | 64/64 |
| Frozen fresh64 tool/status | 21/24 | 24/24 |
| 28 wrapped action prompts | 28/28 | 28/28 |
| E12_A/B | 2/2 | 2/2 |
| E13_A/B | 0/2 | 2/2 |
| S03_B | 0/1 | 1/1 |

Those panels are synthetic development checks, not a public benchmark. The sealed set was written after the training data was frozen, and the new curriculum rows share no 12-word sequence with it. The frozen sets have been used during development; treat them as regression checks, not fresh qualification.

## What it does well

Ask it what a color label means, and it will tell you the meaning has not been supplied instead of inventing one. Give it a definition in the same turn, and it will use yours. Ask how often a review happens when no interval was given, and it will ask for the schedule rather than reach for "every other week." When a later turn corrects an earlier fact, the latest value wins.

Those behaviors came from a 994-row curriculum built around the failures we kept seeing: invented label meanings, invented cadence, ignored corrections. The rest of the 2,028-row training mix replays action schema, interval arithmetic, notice handling and a slice of verified English so the new curriculum does not erase older behavior.

## What it does not do

Arithmetic is still a weak spot. The `E03_A` tape and strip case sends the raw model into a long, inconsistent calculation. There is no arithmetic guard for it, and the card says so.

The raw model can also use a quoted public destination instead of the authorized private home, ignore a supplied recall query, or claim that an errored lookup established absence. The guarded path fixes all three. The weights alone do not.

Long-form factual writing, broad world knowledge, open-ended conversation and RK3588 performance are not qualified. There is no merged HF model or device artifact in this repository. The adapter chain runs on the MLX stack; the base weights are not included.

And the license is non-commercial. This is a research artifact, not a product you can ship.

## Using it

1. Get [Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) under its license.
2. Download the `v81-research-preview` release asset.
3. Apply `adapters/00-v72` through `adapters/10-v81` in the order in [`adapters/ORDER.json`](adapters/ORDER.json).
4. Load the guard from [`guard/`](guard/) and use `guard_action` for saves and recalls. Do not execute a model-authored tool call directly.

The [guard README](guard/README.md) and [`guarded_inference.py`](guard/guarded_inference.py) show the contract. The [model card](MODEL_CARD.md) has the full evaluation, the failure analysis, the training data and the exact hashes.

## Why this exists

SAGE Foundation stewards the specifications and the trust root. SAGE Commons is the fabric that community networks and devices join. Lantern is the first deployment. The model is one piece of that work: local intelligence that keeps a person's knowledge on their device and makes sharing a deliberate act.

A curious mind should not need a better postcode. That line is the whole argument. If the model can answer a useful question in a room with no signal, and keep the answer on the device, the system is doing something worth the effort. If it invents a label meaning or a schedule, the guard and the card should make that visible rather than hide it.

The evaluation and the card are public for the same reason. If the claims are wrong, anyone can check them. If the guard is useful, anyone can reuse it.

## License

The base model and this adapter chain are non-commercial research artifacts under the Qwen Research License. The guard and evaluation code are Apache-2.0. Read [LICENSE](LICENSE), [LICENSE-QWEN-RESEARCH](LICENSE-QWEN-RESEARCH) and [LICENSING.md](LICENSING.md).

## Links

- [Model card](MODEL_CARD.md)
- [V81 research preview release](https://github.com/l33tdawg/lantern-3b/releases/tag/v81-research-preview)
- [SAGE Foundation](https://sage-foundation.net/)
- [SAGE Commons](https://sage.ngo/)

