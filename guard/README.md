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
- `response_guards.label_answer(messages)`: answers an undefined colour/label
  question by asking what the label means in this context. It stays out of the
  way when the conversation supplies a definition.
- `response_guards.cadence_answer(messages)`: asks for a missing check/review
  interval instead of accepting an invented cadence.
- `response_guards.status_text(messages, model_text)`: repairs failed/empty
  lookup absence claims.
- `grounded_longform.compose_grounded_longform(messages)`: deterministically
  composes an exact-paragraph grounded note when the request supplies an
  explicit fact list. It also handles narrow correction and missing-detail
  forms; ordinary chat, code, arithmetic and actions return `None`.

In the deployed server the order is grounded composer, interval, cadence,
label, private-owner refusal, status, then the model. A deterministic answer is
returned before inference.

The response-guard suite covers the interval, cadence, label, status and
paragraph cases. The action guard tests are in the main repository at
`software/runtime/tests/test_action_guard.py` (38 tests); the response-guard
and grounded-composer suites currently run 69 tests plus 20 subtests.

