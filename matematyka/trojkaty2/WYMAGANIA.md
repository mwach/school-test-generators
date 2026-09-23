# Twierdzenie Pitagorasa w zadaniach (matematyka, klasa 8 SP) — `trojkaty2`

Notatka ustaleń dla serii arkuszy „trojkaty2”. Kolejne zestawy (zestaw 2, 3, …) mają się
trzymać tych zasad. Nadrzędne zasady repo: [`../../AGENTS.md`](../../AGENTS.md).
Osobny temat od [`../trojkaty/`](../trojkaty/WYMAGANIA.md) (tamten: obwód/pole/wysokość
trójkąta równobocznego na „niewygodnych” danych) — nie mieszać plików.

## Pochodzenie i zasada tworzenia

- Zamawiający przysłał zdjęcia 2 stron arkusza „Twój zestaw” (Gdańskie Wydawnictwo
  Oświatowe, wybór zadań: Anita Stramel, str. 1–2 z 3; zdjęcia lokalnie:
  `~/Downloads/IMG_2353.jpeg`, `IMG_2354.jpeg` — **nie trafiają do repo**, materiał
  chroniony prawem autorskim).
- Prośba: **„podobny test ze zmienionymi wartościami”** — zachowujemy typ, kolejność
  i formę zadań (rysunki, wybór ABCD, tabela „Tak/Nie, ponieważ 1/2/3”, tabelka do
  uzupełnienia, kratka na obliczenia), ale **wszystkie liczby są nowe**, a treść
  przeformułowana na tyle, na ile pozwala typ zadania.
- W każdym nowym zestawie zmieniaj też **pozycję poprawnej odpowiedzi** w zadaniach
  zamkniętych oraz, gdzie się da, kierunek odpowiedzi (np. zad. 7 w oryginale „Nie”,
  w zestawie 1 „Tak”).

## Oryginał — struktura (wzorzec formy)

| Nr | Typ w oryginale | Wartości w oryginale (nie używać ponownie) |
|---|---|---|
| 1 | 3 rysunki: oblicz *x* (przeciwprostokątna), *y* (przyprostokątna), *z* (wysokość tr. równoramiennego) | 7 i 3; 3 i 3√5; 6, 6, 10 |
| 2 | romb — przekątne dane, oblicz bok | 8 i 6 |
| 3 | pole tr. równoramiennego, wybór ABCD | podstawa 12, ramię 10 |
| 4 | romb — obwód i przekątna AC dane (rysunek), oblicz BD | 52 i 24 |
| 5 | czworokąt z dwóch tr. prostokątnych (kąty proste przy A i B), oblicz CD, wybór ABCD | AB = BC = 1, AD = √2 |
| 6 | wysokość tr. równobocznego | bok 32 |
| 7 | kwadrat o boku √n — czy przekątna ma długość k? Tak/Nie + uzasadnienie 1/2/3 | √18, 3 |
| 8 | tabelka tr. równobocznego (bok, wysokość, obwód, pole); w każdym wierszu dana 1 wielkość | h = 6√3; P = 100√3 |

Trzeciej strony oryginału nie otrzymaliśmy — zestaw ma 8 zadań.

## Zasady doboru wartości (ustalone)

- Wyniki „ładne” albo z jednym pierwiastkiem do uproszczenia (np. √45 = 3√5) — poziom
  jak w oryginale; uczeń nie usuwa niewymierności z mianownika.
- Trójki pitagorejskie w rombach (5-12-13, 6-8-10 itp.), żeby wynik był całkowity.
- Dystraktory w zadaniach zamkniętych odpowiadają typowym błędom: ramię zamiast wysokości,
  pominięte ½, dodanie kwadratów zamiast odejmowania, wynik pośredni (np. BD zamiast CD).
- Rysunki: inline SVG, proporcje zgodne z danymi (skala dowolna), znaczki kąta prostego;
  długość szukanego odcinka **nie** jest podpisana.
- Punktacja: przy każdym zadaniu, suma w nagłówku (`<span data-suma>`), rozpisana w kluczu.

## Pliki

```
trojkaty2.css                          wspólny styl arkusza i klucza
twierdzenie_pitagorasa.html/.pdf       arkusz zestawu 1 (3 strony A4, kratka na obliczenia)
twierdzenie_pitagorasa_klucz.html/.pdf klucz zestawu 1: wzory, rozwiązania krok po kroku, źródła
```

Kolejne zestawy: `twierdzenie_pitagorasa_zestawN.html` + `..._zestawN_klucz.html`.
Arkusz i klucz to **dwa osobne pliki** (zgodnie z `AGENTS.md`).

## Proces

```bash
D=matematyka/trojkaty2
'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' --headless --disable-gpu \
  --no-pdf-header-footer --print-to-pdf=$D/<plik>.pdf "file://$PWD/$D/<plik>.html"
swift historia/kuratorium/tools/pdf_to_png.swift $D/<plik>.pdf <tmp>/podglad 0.9
```

Wszystkie wyniki klucza przelicz niezależnie (np. krótki skrypt `python3 -c ...`) przed
wygenerowaniem PDF; obejrzyj podgląd każdej strony (etykiety na rysunkach nie mogą
nachodzić na odcinki — w zestawie 1 poprawiono etykietę „16 cm” w zad. 4).

## Historia zestawów

| Zestaw | Data | Wartości | Klucz zamknięty |
|---|---|---|---|
| 1 | 2026-09-23 | zad.1: 6 i 3 → x = 3√5; 2 i 2√10 → y = 6; 7, 7, 12 → z = √13 · zad.2: 24 i 10 → 13 · zad.3: 10 i 13 → 60 · zad.4: 40 i 16 → BD = 12 · zad.5: AD = √3 → CD = √5 · zad.6: 26 → 13√3 · zad.7: √32, 8 → Tak · zad.8: h = 4√3; P = 81√3 | 3: B · 5: C · 7: A3 |
