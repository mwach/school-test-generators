# Testy treningowe — Wojewódzki Konkurs Przedmiotowy z Historii

Autorskie arkusze treningowe dla uczniów klas IV–VIII przygotowujących się do Wojewódzkiego
Konkursu Przedmiotowego z Historii organizowanego przez Kujawsko-Pomorskiego Kuratora Oświaty,
wraz z narzędziami, które pomagają je składać i sprawdzać.

Wygenerowane arkusze są **nieoficjalne** — nie pochodzą od kuratorium i nie są jego kluczami.
Odwzorowują natomiast strukturę, punktację i poziom trudności arkuszy archiwalnych: etap szkolny,
19 zadań, dokładnie 100 punktów, 60 minut pracy, zakres materiału zamknięty III rozbiorem (1795 r.).

Komplet zasad — zakres każdego etapu, parametry arkusza, typy zadań, wymagania wobec map,
kluczy i PDF-ów — opisuje [`SPECYFIKACJA_GENEROWANIA_TESTOW_HISTORYCZNYCH.md`](SPECYFIKACJA_GENEROWANIA_TESTOW_HISTORYCZNYCH.md).
To jest dokument nadrzędny; README tylko wprowadza w strukturę repozytorium.

## Gotowe warianty

Każdy wariant to para plików: arkusz dla ucznia (z kartą odpowiedzi) i osobny klucz.
Wszystko, co wygenerowane, leży w `output/` — HTML jako format roboczy, PDF jako docelowy,
pod tą samą nazwą. Wariant G to więc `output/test_szkolny_wariant_G.html`
i `output/test_szkolny_wariant_G.pdf`, a do nich `output/klucz_odpowiedzi_wariant_G.*`.

| Wariant | Pliki w `output/` | Uwagi |
| --- | --- | --- |
| A | `test_szkolny_wariant_A.pdf` + `_poprawiona_mapa` | pierwotna mapa okazała się nieczytelna; wersja poprawiona jest wzorcem jakości map |
| B | `test_szkolny_wariant_B.pdf` | |
| C–F | `test_szkolny_wariant_{C,D,E,F}.pdf` | E jako pierwszy świadomie wykorzystał limit powtórzeń |
| G | `test_szkolny_wariant_G.pdf` | mapa portów hanzeatyckich, „Batory pod Pskowem” Matejki |

Materiały dodatkowe do nauki: `output/Daty_i_wydarzenia_do_nauki.pdf` (chronologia dla ucznia),
`output/Daty_i_wydarzenia_zestawienie.pdf` (pełne zestawienie)
oraz `output/Baza_potencjalnych_pytan.pdf`.

## Struktura repozytorium

W katalogu głównym są tylko dwa dokumenty i cztery katalogi — wszystko, co powstaje
z generowania, trafia do `output/`.

```
output/
  test_szkolny_wariant_*.html      arkusze robocze (źródło PDF-ów)
  klucz_odpowiedzi_wariant_*.html  klucze robocze
  *.pdf                            wersje docelowe arkuszy, kluczy i materiałów do nauki
  baza_pytan.json                  baza zagadnień z oceną ryzyka powtórzenia
  previews/                        podglądy PNG stron — poza repozytorium (.gitignore)
assets/                            mapy SVG, bazowe mapy CC0, reprodukcje obrazów Matejki
tools/                             skrypty pomocnicze (python3 + Swift)
referencje/arkusze/                archiwalne arkusze i klucze kuratorium (2017/2018–2025/2026)
referencje/tekst/                  ich warstwa tekstowa do przeszukiwania
```

Arkusze odwołują się do grafik ścieżką `../assets/…`, więc HTML-a nie należy przenosić
poza `output/` — inaczej mapy i reprodukcje przestaną się wyświetlać.

## Jak powstaje nowy wariant

1. **Dobór tematów.** Punktem wyjścia jest baza zagadnień, która dla każdego wydarzenia
   w zakresie konkursu podaje obszar (historia Polski / powszechna), typ zagadnienia
   i ryzyko powtórzenia względem wcześniejszych arkuszy:

   ```bash
   python3 tools/baza_pytan.py
   ```

   Skrypt czyta arkusze i klucze z `output/`, więc po dodaniu wariantu wystarczy
   uruchomić go ponownie — nic nie trzeba aktualizować ręcznie. Powtórzenia tematów są
   dopuszczalne do 30% zadań (przy 19 zadaniach: najwyżej 5), zawsze w innej formie zadania.

2. **Mapa, jeśli zadanie jej wymaga.** `tools/zbuduj_mape.py` składa mapę z bazowej mapy Europy:
   wypełnia morze i ląd kontrastowo, wycisza granice państw, nanosi ponumerowane punkty
   wyliczone rachunkowo ze współrzędnych geograficznych. Kadr i punkty ustawia się w sekcji
   `__main__`; skrypt przerywa pracę, jeśli punkt wypada poza kadrem.

3. **Arkusz i klucz w HTML** — zapisane w `output/`, zgodnie ze specyfikacją, z rozliczeniem
   limitu powtórzeń w sekcji „Kontrola limitu powtórzeń (30%)” klucza.

4. **Kontrola losowości klucza** przed generowaniem PDF-ów. Narzędzie wykrywa przewidywalne
   klucze (ciągi A, B, C, D oraz 1, 2, 3, 4, pozycje stojące na swoim miejscu, długie serie
   w prawda/fałsz) i kończy się kodem błędu, gdy znajdzie problem:

   ```bash
   python3 tools/sprawdz_losowosc_klucza.py output/klucz_odpowiedzi_wariant_G.html
   ```

   Sprawdzany jest wyłącznie rozkład odpowiedzi, nie ich poprawność — po przetasowaniu banku
   trzeba osobno potwierdzić, że litera z klucza wskazuje właściwe hasło.

5. **PDF** — druk z Chrome w trybie headless:

   ```bash
   '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' \
     --headless --disable-gpu --no-pdf-header-footer \
     --print-to-pdf='output/test_szkolny_wariant_G.pdf' \
     "file://$PWD/output/test_szkolny_wariant_G.html"
   ```

6. **Przegląd składu** — render stron do PNG i obejrzenie ich, zwłaszcza map:

   ```bash
   swift tools/pdf_to_png.swift output/test_szkolny_wariant_G.pdf output/previews/G 0.72
   ```

   Podglądy PNG są celowo wyłączone z repozytorium (`.gitignore`) — odtwarza się je z HTML-a.

Przed oddaniem plików trzeba jeszcze potwierdzić, że suma punktów to dokładnie 100, każde
zadanie ma odpowiedź w kluczu, zakres nie wykracza poza 1795 r., a położenie każdego punktu
na mapie zgadza się z kluczem. Pełna lista kontrolna jest w specyfikacji, w sekcji
„Wymagania dotyczące PDF”.

## Narzędzia

| Skrypt | Do czego służy |
| --- | --- |
| `tools/baza_pytan.py` | baza zagadnień w zakresie konkursu z oceną ryzyka powtórzenia (`--json`, `--html`) |
| `tools/generuj_tabele_daty.py` | chronologiczne zestawienie dat i wydarzeń (`--do-nauki` dla wersji uczniowskiej) |
| `tools/zbuduj_mape.py` | składanie mapy zadania z bazowej mapy Europy |
| `tools/sprawdz_losowosc_klucza.py` | wykrywanie przewidywalnych kluczy odpowiedzi |
| `tools/analizuj_arkusze.py` | zestawienie etapu, liczby zadań, punktacji i czasu pracy arkuszy archiwalnych |
| `tools/extract_pdf_text.swift` | wyciąganie warstwy tekstowej z PDF-ów do przeszukiwania |
| `tools/pdf_to_png.swift` | render stron PDF do PNG, do przeglądu składu |

Skrypty korzystają wyłącznie z narzędzi dostępnych w systemie — `python3` oraz Swift z PDFKit —
bez instalowania dodatkowych zależności. Zakładają macOS (PDFKit, Chrome pod ścieżką `/Applications`).

## Prawa do materiałów

Arkusze i klucze w `referencje/` są dokumentami Kujawsko-Pomorskiego Kuratorium Oświaty
i służą tu wyłącznie jako materiał referencyjny. Bazowe mapy w `assets/` pochodzą z zasobów
CC0 (Natural Earth), reprodukcje obrazów Jana Matejki są w domenie publicznej.
