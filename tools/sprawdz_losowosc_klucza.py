#!/usr/bin/env python3
"""Kontrola przewidywalności klucza odpowiedzi.

Wyłapuje zadania, w których odpowiedzi układają się w ciąg rosnący (A, B, C, D…
albo 1, 2, 3, 4…) lub w długie serie tej samej wartości (P, P, P, P). Taki klucz
pozwala zdobyć punkty bez znajomości materiału.

Użycie:
    python3 tools/sprawdz_losowosc_klucza.py output/klucz_odpowiedzi_wariant_E.html [...]
"""

import re
import sys

MAX_STALYCH = 1          # ile pozycji może stać na swoim miejscu (item n -> n-ta litera)
MAX_ROSNACY_FRAGMENT = 2  # najdłuższy dopuszczalny fragment rosnący
MAX_SERIA_PF = 3          # najdłuższa dopuszczalna seria tej samej wartości w P/F


def zadania(tekst):
    wzor = r'<h3>Zadanie ([IVX]+)\. ([^<]+)</h3>.*?<p class="answer">(.*?)</p>'
    for nr, tytul, odp in re.findall(wzor, tekst, re.S):
        yield nr, tytul.strip(), re.sub(r'<[^>]+>', '', odp)


def najdluzszy_rosnacy(seq):
    naj = biez = 1
    for a, b in zip(seq, seq[1:]):
        biez = biez + 1 if b > a else 1
        naj = max(naj, biez)
    return naj


def najdluzsza_seria(seq):
    naj = biez = 1
    for a, b in zip(seq, seq[1:]):
        biez = biez + 1 if a == b else 1
        naj = max(naj, biez)
    return naj


def sprawdz_zadanie(nr, tytul, odp):
    """Zwraca listę komunikatów o problemach (pusta = zadanie w porządku)."""
    uwagi = []

    litery = re.findall(r'\b\d+\.\s*([A-H])\b', odp)
    if len(litery) >= 4:
        stale = sum(1 for i, l in enumerate(litery) if ord(l) - 65 == i)
        if litery == sorted(litery):
            uwagi.append(f'klucz rosnący {"".join(litery)} – przetasuj bank odpowiedzi')
        elif stale > MAX_STALYCH:
            uwagi.append(f'{stale} pozycji na swoim miejscu w {"".join(litery)}')
        elif najdluzszy_rosnacy(litery) > MAX_ROSNACY_FRAGMENT:
            uwagi.append(f'fragment rosnący dłuższy niż {MAX_ROSNACY_FRAGMENT} w {"".join(litery)}')

    cyfry = [c for _, c in re.findall(r'([A-H])\s*[–-]\s*(\d)', odp)]
    if len(cyfry) >= 4:
        stale = sum(1 for i, c in enumerate(cyfry) if int(c) == i + 1)
        if cyfry == sorted(cyfry):
            uwagi.append(f'klucz rosnący {"".join(cyfry)} – zmień kolejność pozycji w zadaniu')
        elif stale > MAX_STALYCH:
            uwagi.append(f'{stale} pozycji na swoim miejscu w {"".join(cyfry)}')

    pf = re.findall(r'\b\d+\.\s*([PFS])\b', odp)
    if len(pf) >= 4:
        if len(set(pf)) == 1:
            uwagi.append(f'wszystkie odpowiedzi identyczne ({pf[0]})')
        elif najdluzsza_seria(pf) > MAX_SERIA_PF:
            uwagi.append(f'seria dłuższa niż {MAX_SERIA_PF} w {"".join(pf)}')

    return uwagi


def main(pliki):
    bledy = 0
    for plik in pliki:
        tekst = open(plik, encoding='utf-8').read()
        print(f'=== {plik} ===')
        czyste = True
        for nr, tytul, odp in zadania(tekst):
            for uwaga in sprawdz_zadanie(nr, tytul, odp):
                print(f'  BŁĄD  {nr:5s} {tytul[:38]:40s} {uwaga}')
                bledy += 1
                czyste = False
        if czyste:
            print('  OK – żaden klucz nie jest przewidywalny')
    return 1 if bledy else 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
