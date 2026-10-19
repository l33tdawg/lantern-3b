# Lantern 3B V81

A small English model for a computer that fits in your hand.

Lantern is the first device built on SAGE Commons: an offline-first assistant for people and places where the network is thin, expensive, or simply absent. V81 is the research preview of the language model inside it.

The device runtime, touchscreen apps, provisioning tools and offline maps live in the [SAGE Lantern repository](https://github.com/l33tdawg/sage-lantern).

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

Long-form factual writing, broad world knowledge and open-ended conversation are not qualified. V81 still invents meanings and cadences outside the guarded cases; the label guard covers a bounded colour vocabulary, not factuality in general. The merged HF weights are reproducible from the adapter chain, and the base weights are not included.

And the license is non-commercial. This is a research artifact, not a product you can ship.

## Using it

1. Get [Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) under its license.
2. Download the adapter bundle from `v81-research-preview`. For the device build, download `v81-rkllm.part-00` through `v81-rkllm.part-02`.
3. Apply `adapters/00-v72` through `adapters/10-v81` in the order in [`adapters/ORDER.json`](adapters/ORDER.json).
4. Load the guard from [`guard/`](guard/) and use `guard_action` for saves and recalls. Do not execute a model-authored tool call directly.

The [guard README](guard/README.md) and [`guarded_inference.py`](guard/guarded_inference.py) show the contract. The [model card](MODEL_CARD.md) has the full evaluation, the failure analysis, the training data and the exact hashes.

## The build on the device

The release includes the exact RK3588 artifact running on Unit C, our engineering Lantern. It is the V81 merged model converted to W8A8 opt1 and compiled for 16,384 tokens of context, with 8,192 new tokens per response. Download the three parts, check them against `SHA256SUMS.parts`, and reassemble them with [REASSEMBLE.md](REASSEMBLE.md).

The device software, product UI, offline maps and acceptance record are in the [SAGE Lantern repository](https://github.com/l33tdawg/sage-lantern).

On the live 16k/8192 profile, the full 48-request streaming suite completed without a failed request. Median first-token time was 727 ms and median decode was 7.93 tok/s; the 36 quality prompts measured 647 ms and 7.96 tok/s. Those are latency figures from one unit, not a capability or long-form result.

The server applies the label, cadence and interval guards before inference, so a question about an undefined label or interval does not become a confident invention. Requests that supply an explicit fact list and paragraph count go through a deterministic grounded composer instead of the model; the sealed long-form panel passes 20/20 on the deployed unit. The artifact, server and guard hashes, plus the Unit C deployment details, are in [MODEL_ARTIFACTS.md](MODEL_ARTIFACTS.md).

## Why this exists

A curious mind should not need a better postcode. That line is the whole argument. If the model can answer a useful question in a room with no signal, and keep the answer on the device, the system is doing something worth the effort. If it invents a label meaning or a schedule, the guard and the card should make that visible rather than hide it.

Lantern is the first device built on SAGE Commons, and this model is one piece of it. The evaluation and the card are public for the same reason: if the claims are wrong, anyone can check them. If the guard is useful, anyone can reuse it.

## The project around this model

- [SAGE Foundation](https://sage-foundation.net/) stewards the specifications, the trust root and the public interest around the work.
- [SAGE Commons](https://sage.ngo/) is the fabric that community networks and devices join, built on MeshCore transport and the SAGE public chain.
- [Core SAGE project](https://github.com/l33tdawg/sage) is the open implementation the devices and this model build on.
- [SAGE Lantern](https://github.com/l33tdawg/sage-lantern) is the product repository: device runtime, touchscreen apps, provisioning, offline maps and the engineering record.
- [Lantern 3B](https://github.com/l33tdawg/lantern-3b) is this model card, adapter chain, guard and evaluation.

If you are here for the model, start with the [model card](MODEL_CARD.md). If you are here for the project, the core SAGE repo and the Foundation site are the better doors.

## License

The base model and this adapter chain are non-commercial research artifacts under the Qwen Research License. The guard and evaluation code are Apache-2.0. Read [LICENSE](LICENSE), [LICENSE-QWEN-RESEARCH](LICENSE-QWEN-RESEARCH) and [LICENSING.md](LICENSING.md).

## Model links

- [Model card](MODEL_CARD.md)
- [Model artifacts and device build](MODEL_ARTIFACTS.md)
- [Reassemble the RKLLM artifact](REASSEMBLE.md)
- [V81 research preview release](https://github.com/l33tdawg/lantern-3b/releases/tag/v81-research-preview)

