# r4vk-skills

Marketplace ze skillami dla Claude. Każdy skill to osobny plugin z własną wersją.

| Plugin | Działanie |
|---|---|
| [ulepsz-prompt](plugins/ulepsz-prompt/) | zamienia opis celu w jasny prompt |
| [unslop-pl-en](plugins/unslop-pl-en/) | redakcja PL/EN i weryfikacja tłumaczeń |

## Instalacja

**Claude (web, desktop):** Customize → Plugins → Add marketplace → `r4vk/r4vk-skills`. Zainstaluj wybrane pluginy. Włącz „Sync automatically” albo używaj „Check for updates”.

**Claude Code:**

    /plugin marketplace add r4vk/r4vk-skills
    /plugin install ulepsz-prompt@r4vk-skills
    /plugin install unslop-pl-en@r4vk-skills

Pluginy dodane do konta claude.ai pojawiają się też w Claude Code po zalogowaniu na to konto. Wybierz jedną drogę, żeby uniknąć duplikatów.

Aktualizacja w Claude Code: `/plugin marketplace update r4vk-skills`. Auto-update włączysz w menu `/plugin`.

## Przejście ze starego marketplace `unslop-pl-en`

1. Dodaj nowy marketplace.
2. Usuń stary plugin i stary marketplace. W Claude Code: `/plugin marketplace remove unslop-pl-en`.
3. Zainstaluj `unslop-pl-en@r4vk-skills`.
4. Jeśli skill dodano ręcznie (plik `.skill` lub `~/.claude/skills/`), usuń tę kopię.

## Wydanie

1. Zmień pliki w `plugins/<nazwa>/`.
2. Podnieś `version` w `plugins/<nazwa>/.claude-plugin/plugin.json`. Nie dodawaj wersji w `marketplace.json`.
3. Dopisz wpis w `CHANGELOG.md` pluginu.
4. Uruchom `python3 -I scripts/validate.py --base origin/main`.
5. Wypchnij zmiany. Opcjonalnie dodaj tag `<nazwa>--v<wersja>`.

Każda zmiana w folderze pluginu wymaga nowej wersji. CI tego pilnuje, ale nie blokuje pusha na `main`. Pracuj przez PR, jeśli chcesz sprawdzać zmiany przed publikacją.

## Nowy skill

Utwórz `plugins/<nazwa>/.claude-plugin/plugin.json` i `plugins/<nazwa>/skills/<nazwa>/SKILL.md`. Dodaj wpis w `.claude-plugin/marketplace.json`.

## Licencja

MIT.
