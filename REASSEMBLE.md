# Reassemble the RKLLM artifact

Download the three parts from the `v81-research-preview` release, then:

```sh
cat v81-rkllm.part-00 v81-rkllm.part-01 v81-rkllm.part-02 \
  > qwen2_5-vl-3b_fused_w8a8_opt1_ctx16384_rk3588.rkllm
shasum -a 256 qwen2_5-vl-3b_fused_w8a8_opt1_ctx16384_rk3588.rkllm
```

The expected SHA-256 is:

```text
ac7021b61909b9682ea25f21400c195d477c6ad3d2a595adc7d632808dfa6285
```

The parts are split at 1,900,000,000 bytes. The full file is 3,823,749,236
bytes.

This artifact is the RK3588 W8A8 16k device model. It is not a desktop HF
checkpoint and it requires the matching RKLLM runtime.

