# AGENTS.md

Wskazówki dla każdego, kto pracuje w tym repozytorium — człowieka albo agenta. Repozytorium
jest **ogólnym zbiorem zadań/testów z różnych przedmiotów i tematów**, nie projektem
jednego przedmiotu. Zanim zaczniesz cokolwiek generować albo edytować, przeczytaj tę stronę
w całości — jest krótka i oszczędza powtarzania tych samych ustaleń w każdej rozmowie.

## Struktura i zasada izolacji tematów

```
historia/kuratorium/   Wojewódzki Konkurs Przedmiotowy z Historii
matematyka/trojkaty/   geometria trójkątów (klasy 7–8)
chemia/wodorotlenki/   sprawdziany z chemii, klasa 8 — wodorotlenki
```

- Każdy temat = osobny podkatalog pod `historia/`, `matematyka/` albo `chemia/` (albo pod kolejnym
  przedmiotem, gdy się pojawi). Nowy temat nie miesza plików z istniejącym.
- Każdy podkatalog tematu ma własną notatkę ustaleń (`README.md` albo `WYMAGANIA.md`) —
  **przeczytaj ją przed pierwszą zmianą w danym temacie**. Zawiera ustalenia wypracowane
  wcześniej (poziom trudności, konwencje, decyzje zamawiającego), które nie powinny być
  odtwarzane od zera ani przypadkiem cofnięte.
- `historia/kuratorium/` ma dodatkowo dokument nadrzędny —
  `SPECYFIKACJA_GENEROWANIA_TESTOW_HISTORYCZNYCH.md` — ze szczegółowymi wymaganiami
  merytorycznymi. Dla tego tematu to on rozstrzyga w razie wątpliwości, nie README.
- Gotowe narzędzia (`tools/`) leżą dziś fizycznie w `historia/kuratorium/tools/`, ale
  `pdf_to_png.swift` jest współdzielone (matematyka i chemia odwołują się do niego względną ścieżką
  `../../historia/kuratorium/tools/pdf_to_png.swift`). Jeśli narzędzie przestaje być
  specyficzne dla jednego tematu, rozważ przeniesienie go do wspólnego katalogu na poziomie
  repo zamiast kopiowania.

## Wspólny pipeline: HTML → PDF

Niezależnie od tematu:

1. Materiał roboczy to HTML (arkusz zadań i osobny klucz odpowiedzi jako dwa pliki).
2. **Dostawą jest zawsze PDF**, nigdy sam HTML — wygeneruj oba pliki (arkusz, klucz) do PDF
   zanim uznasz zadanie za wykonane.
3. Render przez Chrome headless:
   ```bash
   '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' \
     --headless --disable-gpu --no-pdf-header-footer \
     --print-to-pdf='<sciezka>/plik.pdf' \
     "file://$PWD/<sciezka>/plik.html"
   ```
4. Podgląd PNG stron przed oddaniem pliku (nie tylko generowanie — trzeba **zobaczyć**
   wynik, zwłaszcza mapy/diagramy i podział na strony):
   ```bash
   swift historia/kuratorium/tools/pdf_to_png.swift <sciezka>/plik.pdf <folder_podgladu> 0.9
   ```
   Podglądy PNG nigdy nie trafiają do repo (`.gitignore`) — są odtwarzalne z HTML-a.
5. Ścieżki do grafik/zasobów w HTML-u muszą zostać poprawne względem lokalizacji pliku —
   arkuszy nie przenosi się bez sprawdzenia, czy odwołania (`../assets/…` itp.) wciąż działają.

Narzędzia zakładają macOS (PDFKit, Chrome pod `/Applications`) i nie instalują żadnych
zależności poza `python3` i Swift dostępnym w systemie — trzymaj się tego ograniczenia przy
dodawaniu nowych skryptów, żeby pipeline pozostał zero-dependency.

## Zasady wspólne dla treści (dowolny przedmiot)

- **Nigdy nie zmyślaj faktów.** Każda odpowiedź w kluczu musi być zweryfikowana w co najmniej
  jednym wiarygodnym źródle; fakty niejednoznaczne — w dwóch niezależnych źródłach. Podawaj
  aktywne adresy URL źródeł w kluczu.
- **Materiały archiwalne/referencyjne to wzorzec formy, nie bank pytań** — chyba że dokument
  tematu wyraźnie pozwala zapożyczać wprost z konkretnego, ograniczonego źródła (tak jak dla
  historii: banki mazowiecki/pomorski/zachodniopomorski, do 30–50% zadań, patrz specyfikacja).
  Domyślnie zakładaj zakaz kopiowania treści zadań.
- **Klucz musi mieć jednoznaczną, sprawdzoną punktację** — suma punktów zgodna z deklaracją
  na stronie tytułowej, każde zadanie ma odpowiedź w kluczu, brak odpowiedzi dopuszczających
  więcej niż jedno rozwiązanie, jeśli polecenie tego nie przewiduje.
- **Losowa/nieprzewidywalna kolejność odpowiedzi w kluczu, gdziekolwiek to zastosowanie ma
  sens** (dopasowania, wybór jednokrotny, prawda/fałsz, chronologia, mapy). Klucz nie może
  dać się odgadnąć ze wzorca (ciąg rosnący A,B,C,D / 1,2,3,4, długie serie tej samej wartości).
  Dla historii istnieje gotowy kontroler: `tools/sprawdz_losowosc_klucza.py`, uruchamiany
  **przed** generowaniem PDF — analogiczny automatyczny check warto dodać dla każdego nowego
  tematu, który ma losowane klucze, zamiast polegać wyłącznie na przeglądzie ręcznym.
- **Po każdym przetasowaniu banku odpowiedzi sprawdź merytorycznie**, że litera/numer z klucza
  nadal wskazuje właściwe hasło — przetasowanie samej kolejności bez weryfikacji jest częstym
  źródłem błędów.
- **Grafiki i mapy**: preferuj domenę publiczną / CC0 / Creative Commons z wiarygodnego
  repozytorium, podawaj autora, repozytorium i licencję. Mapy geograficzne rysuj na bazie
  poprawnej mapy wektorowej (nie odręcznie), z wysokim kontrastem lądu/morza/granic i bez
  podpowiedzi zdradzających odpowiedź.
- **Przed oddaniem pliku** zawsze: otwórz wygenerowany PDF (lub jego podgląd PNG), sprawdź że
  ma wszystkie strony i ilustracje, że nic nie jest przycięte, że klucz zaczyna się czytelnie
  oddzielony od arkusza zadań. Nie zgłaszaj zadania jako wykonane na podstawie samego
  wygenerowania pliku, bez wizualnej weryfikacji.
- Notatki (`README.md`/`WYMAGANIA.md`) tematu **aktualizuj razem ze zmianą ustaleń** — jeśli
  podejmujesz decyzję, która obowiązuje przyszłe warianty/zadania z tego tematu (nowy poziom
  trudności, nowa konwencja nazewnictwa, nowe ograniczenie), zapisz ją tam, a nie tylko w
  wiadomości do użytkownika — inaczej następna sesja odtwarza tę samą dyskusję od zera.

## Konwencje repozytorium (git, pliki)

- Commity po polsku, krótki tytuł w trybie rozkazującym (`Dodaj…`, `Przenieś…`, `Popraw…`),
  zgodnie z dotychczasową historią (`git log --oneline`).
- Nie twórz commitów bez wyraźnej prośby użytkownika; nie używaj `--force`, `--amend` na
  opublikowanych commitach ani innych operacji niszczących bez wyraźnej zgody.
- Pliki robocze (podglądy PNG, cache Pythona) są wyłączone przez `.gitignore` — nie commituj
  ich ręcznie i nie zdejmuj wpisu z `.gitignore`, żeby je wymusić.
- Zanim przeniesiesz/zmienisz strukturę katalogów, sprawdź wszystkie odwołania względne w
  plikach, które się przenoszą (linki w Markdown, ścieżki `src=`/`href=` w HTML-u, ścieżki w
  skryptach) — przeniesienie samego pliku bez poprawek ścieżek cicho psuje pipeline.
- Jeżeli dodajesz nowy temat, dodaj go też do listy w głównym [`README.md`](README.md).
