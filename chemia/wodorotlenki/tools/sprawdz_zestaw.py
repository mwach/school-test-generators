#!/usr/bin/env python3
"""Kontrola zestawu sprawdzianu z wodorotlenków: punktacja i losowość klucza.

Sprawdza dla każdej grupy:
  * suma data-pkt zadań w arkuszu == zadeklarowana suma (<span data-suma>),
  * każde zadanie z arkusza ma pozycję w kluczu z tą samą punktacją,
  * odpowiedzi zamknięte w kluczu (<span class="zamkniete" data-typ=...>) nie układają
    się w przewidywalny wzór: P/F — seria tej samej wartości > 3 albo pełna naprzemienność;
    wybór jednokrotny — wszystkie odpowiedzi tą samą literą; wybór wielokrotny —
    litery kolejne (A, B, C).

Użycie (z katalogu repo):
    python3 chemia/wodorotlenki/tools/sprawdz_zestaw.py chemia/wodorotlenki/sprawdzian_wodorotlenki_zestaw1
Argument to wspólny prefiks plików: <prefiks>_grupa_X.html i <prefiks>_klucz.html.
"""

import glob
import re
import sys

MAX_SERIA_PF = 3


def najdluzsza_seria(seq):
    naj = biez = 1
    for a, b in zip(seq, seq[1:]):
        biez = biez + 1 if a == b else 1
        naj = max(naj, biez)
    return naj


def zadania(html):
    return {int(z): int(p) for z, p in re.findall(r'data-zad="(\d+)" data-pkt="(\d+)"', html)}


def main(prefiks):
    klucz = open(f'{prefiks}_klucz.html', encoding='utf-8').read()
    bloki = dict(re.findall(r'data-grupa="([A-Z])">(.*?)(?=data-grupa="|<h2>Źródła)', klucz, re.S))
    arkusze = sorted(glob.glob(f'{prefiks}_grupa_*.html'))
    if not arkusze:
        sys.exit(f'Brak arkuszy {prefiks}_grupa_*.html')
    bledy = []
    for sciezka in arkusze:
        grupa = re.search(r'_grupa_([A-Z])\.html$', sciezka).group(1)
        html = open(sciezka, encoding='utf-8').read()
        ark = zadania(html)
        suma = int(re.search(r'data-suma>(\d+)<', html).group(1))
        if sum(ark.values()) != suma:
            bledy.append(f'{grupa}: suma punktów zadań {sum(ark.values())} ≠ deklarowane {suma}')
        blok = bloki.get(grupa)
        if blok is None:
            bledy.append(f'{grupa}: brak sekcji w kluczu')
            continue
        kl = zadania(blok)
        for z, p in ark.items():
            if z not in kl:
                bledy.append(f'{grupa}: zadanie {z} nie ma odpowiedzi w kluczu')
            elif kl[z] != p:
                bledy.append(f'{grupa}: zadanie {z} — arkusz {p} pkt, klucz {kl[z]} pkt')
        for z in kl.keys() - ark.keys():
            bledy.append(f'{grupa}: w kluczu jest zadanie {z}, którego nie ma w arkuszu')

        zamkniete = re.findall(r'class="zamkniete" data-typ="(\w+)">([^<]+)<', blok)
        pojedyncze = []
        for typ, odp in zamkniete:
            wartosci = [w.strip() for w in odp.split(',')]
            if typ == 'pf':
                if najdluzsza_seria(wartosci) > MAX_SERIA_PF:
                    bledy.append(f'{grupa}: seria P/F dłuższa niż {MAX_SERIA_PF}: {odp}')
                if len(wartosci) >= 4 and najdluzsza_seria(wartosci) == 1:
                    bledy.append(f'{grupa}: P/F idealnie naprzemienne: {odp}')
            elif typ == 'wybor':
                pojedyncze += wartosci
            elif typ == 'wielokrotny':
                kody = [ord(w) for w in wartosci]
                if len(kody) >= 3 and all(b - a == 1 for a, b in zip(kody, kody[1:])):
                    bledy.append(f'{grupa}: wybór wielokrotny to kolejne litery: {odp}')
        if len(pojedyncze) >= 2 and len(set(pojedyncze)) == 1:
            bledy.append(f'{grupa}: wszystkie odpowiedzi jednokrotnego wyboru to {pojedyncze[0]}')
        print(f'{grupa}: {len(ark)} zadań, {sum(ark.values())}/{suma} pkt, '
              f'odpowiedzi zamknięte: {"; ".join(o for _, o in zamkniete)}')

    if bledy:
        print('\nPROBLEMY:')
        for b in bledy:
            print(' -', b)
        sys.exit(1)
    print('OK — punktacja spójna, klucz bez przewidywalnych wzorów.')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
