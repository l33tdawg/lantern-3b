# Guard usage

The guard is part of the preview. The model proposes text; the runtime owns
the canonical action, values, authorization and execution.

- `action_guard.guard_action(request_json, model_text, routing_json)`:
  canonicalizes a trusted save or recall request. Saves use
  `canonical_save`; recalls use `canonical_recall`. Supplied recall queries are
  used even when the model asks for one. Quoted text is never authority.
- `action_guard.render(result)`: renders a canonical `<tool_call>` for the
  dispatcher. Execute only this canonical call, never the model's raw text.
- `response_guards.interval_answer(messages)`: canonicalizes the published
  interval/rate cases.
- `response_guards.status_text(messages, model_text)`: repairs failed/empty
  lookup absence claims.

The action guard tests are in the main repository at
`software/runtime/tests/test_action_guard.py` (38 tests).

