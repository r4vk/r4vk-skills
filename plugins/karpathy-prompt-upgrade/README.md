# Karpathy Prompt Upgrade

Turns a goal description or a draft into a copy-ready prompt. It works only on an explicit request, e.g. "upgrade my prompt: …". It does not perform the task unless asked.

The skill is written in English and replies in the user's language, including the upgraded prompt. Ask for another language if you need one. The writing rules are based on ASD-STE100. That standard covers English only, and the skill claims no compliance.

The name is a nod to Andrej Karpathy. This project is not affiliated with or endorsed by him.

## Tests

Test cases are in `evals/`. Run them from the plugin directory (paid model calls):

    claude plugin eval .

Before you change a rule, add a case that shows the problem. Compare the results with a run without the plugin.

## Install

    /plugin marketplace add r4vk/r4vk-skills
    /plugin install karpathy-prompt-upgrade@r4vk-skills

For other methods, see the [marketplace README](../../README.md).
