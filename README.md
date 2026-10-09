# Zadania i testy

Repozytorium z autorskimi materiałami edukacyjnymi do różnych przedmiotów i tematów —
arkuszami zadań, kluczami odpowiedzi i narzędziami, które pomagają je składać i sprawdzać.
Każdy temat ma własny podkatalog z kompletem plików i własną notatką (README/WYMAGANIA)
opisującą ustalenia specyficzne dla tego tematu.

Materiały są autorskie/treningowe, chyba że plik wyraźnie mówi inaczej (np. archiwalne
arkusze kuratoryjne w `historia/kuratorium/referencje/` — te są materiałem referencyjnym,
nie naszą twórczością). Zob. **Prawa do materiałów** niżej.

Zasady pracy nad repozytorium (dla ludzi i agentów) są w [`AGENTS.md`](AGENTS.md) —
to dokument nadrzędny dla konwencji wspólnych wszystkim tematom.

## Struktura repozytorium

```
historia/kuratorium/   arkusze treningowe do Wojewódzkiego Konkursu Przedmiotowego z Historii
matematyka/trojkaty/   arkusze zadań z geometrii trójkątów
matematyka/trojkaty2/  twierdzenie Pitagorasa: trójkąty, romb, kwadrat
chemia/wodorotlenki/   sprawdziany z chemii (klasa 8): wodorotlenki
fizyka/drgania/        testy z fizyki: drgania (3 rozdziały, baza pytań + generator)
AGENTS.md              konwencje wspólne całemu repozytorium (dla ludzi i agentów)
```

Każdy nowy temat (kolejny przedmiot albo kolejne zagadnienie w istniejącym przedmiocie)
dostaje własny podkatalog na tym samym poziomie, np. `historia/<kolejny-temat>/` albo
`matematyka/<kolejny-temat>/` — nie miesza się materiałów różnych tematów w jednym folderze.

## Tematy

### `historia/kuratorium/`

Autorskie arkusze treningowe dla klas IV–VIII przygotowujących się do Wojewódzkiego Konkursu
Przedmiotowego z Historii (Kujawsko-Pomorski Kurator Oświaty). Gotowe warianty, pełna
specyfikacja generowania, archiwum referencyjne arkuszy kuratoryjnych i narzędzia
(python3 + Swift) do budowy map, doboru tematów, kontroli losowości klucza i renderowania PDF.

Zacznij od [`historia/kuratorium/README.md`](historia/kuratorium/README.md) — opisuje gotowe
warianty i strukturę katalogu. Dokumentem nadrzędnym (zasady, zakres, punktacja, wymagania wobec
map i kluczy) jest
[`historia/kuratorium/SPECYFIKACJA_GENEROWANIA_TESTOW_HISTORYCZNYCH.md`](historia/kuratorium/SPECYFIKACJA_GENEROWANIA_TESTOW_HISTORYCZNYCH.md).

### `matematyka/trojkaty/`

Arkusze zadań z geometrii trójkątów (na razie: trójkąt równoboczny — obwód, pole, wysokość)
dla klas 7–8, z kluczem zawierającym pełne rozwiązania krok po kroku. Ten sam pipeline
generowania PDF co w `historia/kuratorium/`.

Zacznij od [`matematyka/trojkaty/WYMAGANIA.md`](matematyka/trojkaty/WYMAGANIA.md) — poziom
trudności, struktura arkusza, konwencje.

### `matematyka/trojkaty2/`

Test z zastosowań twierdzenia Pitagorasa (trójkąty prostokątne, równoramienne, równoboczne,
romb, kwadrat) dla klasy 8 — forma wzorowana na przysłanym arkuszu, wartości zmienione;
osobny klucz z rozwiązaniami krok po kroku.

Zacznij od [`matematyka/trojkaty2/WYMAGANIA.md`](matematyka/trojkaty2/WYMAGANIA.md).

### `chemia/wodorotlenki/`

Sprawdziany z chemii dla klasy 8 SP z działu „Wodorotlenki” (nazewnictwo, wzory sumaryczne,
reakcje otrzymywania, właściwości NaOH i KOH, dysocjacja) — grupy A i B, osobny klucz ze źródłami,
kontroler punktacji i losowości klucza (`tools/sprawdz_zestaw.py`).

Zacznij od [`chemia/wodorotlenki/WYMAGANIA.md`](chemia/wodorotlenki/WYMAGANIA.md) — zakres,
bank związków, rozstrzygnięte konwencje, historia zestawów.

### `fizyka/drgania/`

Testy z fizyki z działu „Drgania” (3 rozdziały × 2 zadania: obliczenia, P/F, quiz) z osobną kartą
odpowiedzi. Baza pytań `baza_pytan.json` powstała na podstawie skanów podręcznika; generator
`tools/generuj_test.py` losuje zadania, zmienia dane liczbowe i kontroluje losowość klucza.

Zacznij od [`fizyka/drgania/WYMAGANIA.md`](fizyka/drgania/WYMAGANIA.md).

## Wspólny pipeline generowania PDF

Każdy temat trzyma się tego samego wzorca: HTML jest formatem roboczym, PDF jest jedynym
dopuszczalnym formatem dostawy (arkusz + osobny klucz). Render przez Chrome headless:

```bash
'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf='<sciezka>/plik.pdf' \
  "file://$PWD/<sciezka>/plik.html"
```

Podgląd stron PDF do weryfikacji składu (Swift + PDFKit, tylko macOS) —
narzędzie leży w `historia/kuratorium/tools/`, jest współdzielone przez wszystkie tematy:

```bash
swift historia/kuratorium/tools/pdf_to_png.swift <sciezka>/plik.pdf <folder_podgladu> 0.9
```

Szczegóły i pełne listy kontrolne — w dokumentach każdego tematu.

## Prawa do materiałów

- Autorskie arkusze, klucze i notatki w tym repozytorium są naszą twórczością.
- Archiwalne arkusze kuratoryjne w `historia/kuratorium/referencje/arkusze/` są dokumentami
  odpowiednich kuratoriów oświaty i służą wyłącznie jako materiał referencyjny/kalibracyjny
  (część z nich — mazowieckie, pomorskie, zachodniopomorskie — decyzją zamawiającego wolno
  też cytować wprost w ograniczonym zakresie; zasady w
  [`SPECYFIKACJA_GENEROWANIA_TESTOW_HISTORYCZNYCH.md`](historia/kuratorium/SPECYFIKACJA_GENEROWANIA_TESTOW_HISTORYCZNYCH.md)).
- Bazowe mapy w `historia/kuratorium/assets/` pochodzą z zasobów CC0 (Natural Earth,
  Wikimedia Commons), reprodukcje obrazów Jana Matejki są w domenie publicznej.
