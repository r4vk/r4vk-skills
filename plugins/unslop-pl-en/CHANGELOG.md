# Changelog

Versions follow semantic versioning. Bump `version` in `.claude-plugin/plugin.json` for every release.

## 0.1.1

Moved to the `r4vk-skills` marketplace. Only change in the skill: angle brackets removed from the description (PL-EN).

## 0.1.0

First release.

- Skill `unslop-pl-en`: Write, Check, Rewrite, Edit file, Translate and Verify translation modes for Polish and English.
- Three levels (words, rhythm, structure), register profiles, guardrails against invented or lost content.
- Polish reference: calques, register, address form, tense against dates, aspect, typography.
- English reference: word tiers, patterns, issues common to Polish authors.
- Translation protocol with a fact ledger and verification step; PL<->EN glossary for IT, AI regulation and the Polish energy market.
- `scripts/lint.py`: mechanical checks (quotation marks, dashes, address form, tense against dates, contrast patterns, slogan runs, word lists) with unit tests.
