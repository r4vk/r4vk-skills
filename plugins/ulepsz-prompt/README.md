# ulepsz-prompt

Zamienia opis celu lub szkic w prompt gotowy do skopiowania. Działa na wyraźną prośbę, np. „ulepsz prompt: …”. Nie wykonuje zadania bez polecenia.

Domyślny język promptu to polski. Zasady pisania są inspirowane ASD-STE100. Polski tekst nie jest zgodny z tym standardem.

## Testy

Przypadki leżą w `evals/`. Uruchomienie (płatne wywołania modelu), z katalogu pluginu:

    claude plugin eval .

Przed zmianą reguły dodaj przypadek, który pokazuje problem. Porównaj wyniki z wersją bez pluginu.

## Instalacja

    /plugin marketplace add r4vk/r4vk-skills
    /plugin install ulepsz-prompt@r4vk-skills

Inne sposoby opisuje [README marketplace](../../README.md).
