# Arkusze zadań — trójkąt równoboczny (obwód, pole, wysokość)

Notatka z ustaleń wypracowanych podczas tworzenia pierwszego arkusza
(`trojkat_rownoboczny.pdf`), żeby kolejne warianty/tematy
z geometrii trójkątów trzymały się tych samych zasad bez powtarzania dyskusji.

## Grupa docelowa i zakres

- Klasa 7–8 szkoły podstawowej.
- Temat: trójkąt równoboczny — obwód (L = 3a), wysokość (h = a√3/2), pole (P = a²√3/4).
- 5–6 zadań na arkusz, punktacja przy każdym zadaniu (suma podana w nagłówku, np. „Liczba punktów: ___/18”).

## Poziom trudności — wymóg kluczowy

Dane w zadaniach (bok, obwód lub wysokość) **powinny zawierać pierwiastki lub ułamki
zwykłe**, a nie tylko liczby całkowite — chodzi o to, żeby uczeń ćwiczył samo
wykonywanie działań na takich wyrażeniach, nie tylko podstawianie do wzoru:

- mnożenie pierwiastków: √a · √b = √(a·b) — np. bok 2√6 cm we wzorze na wysokość,
- wyłączanie czynnika przed pierwiastek — np. bok podany jako √48 cm (trzeba
  uprościć do 4√3 przed dalszymi obliczeniami),
- potęgowanie i mnożenie ułamków zwykłych — np. bok 3/4 dm w polu, gdzie trzeba
  policzyć (3/4)² i pomnożyć przez √3/4,
- zadanie odwrotne (dana wysokość → szukany bok) tak dobrane, żeby pierwiastek
  się skracał do „ładnego” wyniku (uczeń nie musi jeszcze usuwać niewymierności
  z mianownika — to wykracza poza poziom 7–8 klasy),
- jedno zadanie tekstowe (kontekst praktyczny) łączące obwód i pole na tych
  samych, „niewygodnych” danych (pierwiastek lub ułamek).

Wersja z samymi liczbami całkowitymi (pierwszy szkic) została uznana za zbyt
łatwą i odrzucona — to jest ustalony, docelowy poziom trudności dla tej serii
arkuszy, nie jednorazowa decyzja.

## Struktura arkusza

1. **Nagłówek**: tytuł, podtytuł z poziomem/klasą, pole na imię i nazwisko,
   klasę, datę, liczbę punktów.
2. **Diagram** trójkąta (inline SVG) z opisanymi bokami `a` i wysokością `h`
   (linia przerywana od wierzchołka do podstawy).
3. **Zadania** — każde w osobnej „karcie” (ramka, nagłówek z numerem i
   punktacją, treść, miejsce na odpowiedź z kropkowaną linią).
4. **Brak wzorów i przypomnień reguł na arkuszu zadań** — to świadoma decyzja:
   arkusz ma testować, czy uczeń pamięta/umie wyprowadzić, a nie podpowiadać
   w trakcie rozwiązywania.
5. **Podział stron**: arkusz zadań, potem `page-break`, potem klucz.
6. **Klucz odpowiedzi** (osobna strona/strony):
   - na początku klucza umieszczamy sekcję ze wzorami (L=3a, h=a√3/2, P=a²√3/4)
     oraz krótkie przypomnienie reguł (mnożenie pierwiastków, wyłączanie
     czynnika, potęgowanie/mnożenie ułamków) — to miejsce na „ściągawkę”,
     nie arkusz zadań,
   - dalej pełne rozwiązania krok po kroku dla każdego zadania (nie tylko
     wynik końcowy), z wynikiem dokładnym i przybliżeniem dziesiętnym tam,
     gdzie to naturalne (przyjmować √3 ≈ 1,73 / √2 ≈ 1,41 itp.).

## Proces techniczny generowania PDF

Ten sam pipeline co reszta repozytorium (opisany w głównym `README.md`):

1. Przygotować/edytować plik `.html` (styl zbliżony do arkuszy historycznych:
   granat #163a63/#1f5a91 jako kolor główny, pomarańcz #9a5a00 jako akcent —
   ale układ uproszczony, bez elementów specyficznych dla testu historycznego
   typu „instructions”, „choices” itp.).
2. Wydruk do PDF przez Chrome headless:
   ```bash
   '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' \
     --headless --disable-gpu --no-pdf-header-footer \
     --print-to-pdf='<sciezka>/plik.pdf' \
     "file://$PWD/<sciezka>/plik.html"
   ```
3. Podgląd stron do weryfikacji składu:
   ```bash
   swift ../../historia/kuratorium/tools/pdf_to_png.swift <sciezka>/plik.pdf <folder_podgladu> 0.9
   ```
4. Sprawdzić wizualnie (przez odczyt PNG), że: zadania nie są przycięte,
   liczba stron jest sensowna (arkusz nie generuje pustych/prawie pustych
   stron z powodu przelewającego się `footer-note`), klucz odpowiedzi
   zaczyna się od nowej strony.

## Lokalizacja plików

- Gotowe arkusze (HTML + PDF) trzymamy bezpośrednio w `matematyka/trojkaty/`,
  osobno od materiałów historycznego konkursu w `historia/kuratorium/`, żeby
  nie mieszać tematów w tym samym folderze.
- Ta notatka (`matematyka/trojkaty/WYMAGANIA.md`) to miejsce na kontekst i
  ustalenia dotyczące **tematu trójkątów** — kolejne warianty/zadania z tej
  serii powinny się do niej odwoływać zamiast odtwarzać ustalenia od zera.
