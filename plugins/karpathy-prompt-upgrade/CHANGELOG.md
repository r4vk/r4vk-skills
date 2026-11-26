# Changelog

## 0.2.0

- Renamed from `ulepsz-prompt` to `karpathy-prompt-upgrade`.
- Skill, documentation and test cases translated into English.
- New "Response language" section: everything the user sees, including the prompt, is in the user's language. Before, the prompt defaulted to Polish.
- New test case for a Polish request.

## 0.1.0

First version.

- Two modes: quick and full (at most 5 questions in the first round).
- 12 internal questions; facts kept apart from assumptions.
- Writing rules based on ASD-STE100 (no compliance claimed).
- 5 test cases in `evals/`.
