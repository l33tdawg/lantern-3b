# Model artifacts

This preview ships in three forms.

## 1. Adapter chain

`adapters/00-v72` through `adapters/10-v81` are the ordered MLX LoRA chain.
`adapters/ORDER.json` records the order and SHA-256 of every adapter. This is
the source recipe and the smallest download.

## 2. Merged HF source

The chain was fused into the publisher layout for RKLLM conversion. The merged
`model.safetensors` has:

- SHA-256: `a94aec13c01ea176fb9c467997c4224fe1d0f485e877577848f62140290d00ce`
- Bytes: `7,509,337,686`
- Tensors: 824, bfloat16

The merged HF weights are not a separate release asset. `MERGE_RECEIPT.public.json`
records the base index, parent adapter hashes and merged digest. Rebuild them by
applying the adapter chain in order to Qwen2.5-VL-3B-Instruct.

## 3. RKLLM device artifact

The model running on the Lantern engineering device (Unit C) is the W8A8
quantized artifact:

- File: `qwen2_5-vl-3b_fused_w8a8_opt1_ctx16384_rk3588.rkllm`
- SHA-256: `ac7021b61909b9682ea25f21400c195d477c6ad3d2a595adc7d632808dfa6285`
- Bytes: `3,823,749,236`
- Quantization: W8A8 opt1
- Compiled context: 16,384 tokens
- Served `max_new_tokens`: 8,192

The release splits this file into `v81-rkllm.part-00`, `v81-rkllm.part-01` and
`v81-rkllm.part-02`. See `REASSEMBLE.md`.

### Unit C deployment

- Service: `sage-lantern-llm.service`, loopback port 8081
- Model id served for compatibility: `lantern-native5-2b`
- Engine: token engine `11fcb514…`
- Response guard: `ac69b131412ada129483c9003e301f5fb930ed37536919a3ec4ca90fd199ae07`
- Server: `40f14b71e4f2e729c811290b297fbcdb06db7ebc6fe021caf6532581ee028ec8`
- Health: `/health` returns `{"status":"ok"}`
- Guard check: E13_A, E13_B and S03_B pass
- Benchmark: 48/48 streaming requests; 726.7 ms median TTFT, 7.93 tok/s
  median decode across all requests; the 36 quality prompts measured 646.9 ms
  and 7.96 tok/s

The token engine loads only one 3B lane at a time. V79.6 remains on disk as the
rollback model; remove the V81 drop-in to return to it.

