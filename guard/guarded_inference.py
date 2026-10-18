"""Minimal guarded-call example for the V81 research preview.

This file shows the contract, not a complete MLX model loader. Load the base
model and the adapter chain in the order in adapters/ORDER.json, then use the
guard around every action.
"""
from __future__ import annotations

import json

from action_guard import guard_action, render
from response_guards import interval_answer, status_text


def guarded_action(request: dict, model_text: str, routing: dict) -> dict:
    request_json = json.dumps(request, separators=(",", ":"))
    routing_json = json.dumps(routing, separators=(",", ":"))
    result = guard_action(request_json, model_text, routing_json)
    if result.kind == "tool_call":
        return {"kind": "tool_call", "call": result.tool_call, "text": render(result)}
    if result.kind in {"clarification", "error"}:
        return {"kind": result.kind, "text": result.text, "reason": result.reason}
    return {"kind": "pass", "text": result.text}


def guarded_status(messages: list[dict], model_text: str) -> str:
    interval = interval_answer(messages)
    if interval:
        return interval
    return status_text(messages, model_text)


if __name__ == "__main__":
    example_request = {
        "action": "recall",
        "query": "notes about the mock woven-disk frame",
        "scope": "auto",
        "top_k": 4,
        "min_confidence": 0.6,
    }
    example_routing = {
        "owned_home": "self",
        "permitted_public_domains": [],
        "private_grants": [],
    }
    print(json.dumps(guarded_action(
        example_request, "What would you like me to look up?", example_routing),
        indent=2))
