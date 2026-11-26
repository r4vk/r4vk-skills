# unslop-pl-en

A Claude skill that keeps Polish and English text from reading as AI-generated, and keeps translations between the two faithful.

*Skill dla Claude, który pilnuje, żeby polskie i angielskie teksty nie brzmiały jak wygenerowane przez AI, a tłumaczenia PL<->EN zachowywały treść.*

## What it does

- **Write, Check, Rewrite, Edit file:** works on three levels (words, sentence rhythm, structure), with strictness profiles per register (web copy, bio/CV, article, email, docs, academic, slides).
- **Polish-specific rules:** calques from English ("praktyk dostarczania" for *delivery practitioner*, "butikowy", "adresować problem"), colloquial verbs in professional copy, address form (Ty / Wy / Państwo) kept to one per document, past tense for roles that ended, aspect, quotation marks „…”, dashes, non-breaking spaces.
- **English rules:** word tiers, contrast patterns ("not X, it's Y"), kickers, and issues typical for Polish authors (false friends, nominal stacks).
- **Invented-opponent rule:** "Praktyk wdrożeń, nie teoretyk norm" is replaced by a plain statement of what the person does, from facts in the text.
- **Translate and Verify translation (PL<->EN):** builds a fact ledger (numbers, names, dates, hedges, negations, scope), translates meaning rather than construction, then checks the result against the ledger. Gaps are reported, never filled in.
- **Guardrails:** no invented facts, no lost claims, no change in strength ("około" stays approximate, "do 25" stays "up to 25"), voice preserved, minimal edits.
- **Linter** (`scripts/lint.py`): deterministic checks for what a model reads past. Candidates only; the model judges in context.

It is not a tool for evading AI detectors or disclosure duties.

## Install

    /plugin marketplace add r4vk/r4vk-skills
    /plugin install unslop-pl-en@r4vk-skills

Other surfaces: see the [marketplace README](../../README.md).

## Use

Just ask. Examples:

```
Popraw ten tekst, brzmi jak AI: <tekst>
Sprawdź, co w tym tekście wygląda na wygenerowane (tylko lista, bez poprawek)
Przetłumacz na angielski i sprawdź, że niczego nie zgubiłeś
Does this read like AI? <text>
Translate to Polish and verify the numbers and hedges
```

Run the linter yourself:

```bash
python3 -I skills/unslop-pl-en/scripts/lint.py page.html
python3 -I skills/unslop-pl-en/scripts/lint.py draft.md --lang pl --json
```

## Layout

```
.claude-plugin/plugin.json
skills/unslop-pl-en/   SKILL.md, references/, scripts/lint.py, evals/cases.md
tests/test_lint.py
```

## Customize

- Add terms to `references/glossary.md` (one preferred rendering per row).
- Add stock phrases and calques to `references/polish.md` or `english.md`, and a regex to `scripts/lint.py` if the pattern is mechanical.
- When you add a rule, add one example it must catch and one look-alike it must leave alone to `evals/cases.md`.

## Releasing

Change the skill, update `evals/cases.md`, then follow the release steps in the [marketplace README](../../README.md).

## Credits

Inspired by [no-ai-slop](https://github.com/petergyang/no-ai-slop) by Peter Yang and [unslop](https://github.com/jlwin/unslop_ai) by Jean-Luc Winkler (both MIT). The rules, lists and examples here are written for Polish and English; no text is copied.

## License

MIT, see [LICENSE](LICENSE).
