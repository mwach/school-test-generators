#!/usr/bin/env python3
"""Budowanie map konkursowych z bazowej mapy Europy (Natural Earth 1:50 mln, CC0).

Mapa bazowa `assets/europe_blank_cc0.svg` ma 50 ścieżek: 49 cieńszych (stroke-width 0.6) to
granice państw, a jedna grubsza (0.9) to linia brzegowa całego lądu. Dzięki temu można
wypełnić ląd i morze różnymi kolorami — bez tego mapa jest białą plątaniną wielokątów,
w której uczeń nie odróżnia morza od lądu (defekt mapy wariantu F).

Położenie punktów liczone jest rachunkowo z odwzorowania Mercatora dopasowanego do mapy
bazowej, a nie szacowane na oko.

Użycie: patrz sekcja `if __name__ == '__main__'` — konfiguracja konkretnej mapy jest w kodzie,
bo każde zadanie ma inny kadr, inne punkty i inną legendę.
"""
import math
import pathlib
import re

BAZA = pathlib.Path(__file__).parent.parent / 'assets' / 'europe_blank_cc0.svg'

# Odwzorowanie Mercatora mapy bazowej (§12 specyfikacji): dopasowane do 17 stolic
# z maksymalnym błędem 0,13 piksela.
MERC_A = 1374.20
MERC_B = 496.33
MERC_C = 1374.18
MERC_D = 2809.24

KOLOR_MORZA = '#cfe2ee'
KOLOR_LADU = '#f7f3e8'
KOLOR_BRZEGU = '#41525f'
KOLOR_GRANIC = '#b9c2ca'


def na_piksele(lon, lat):
    """Współrzędne geograficzne -> układ mapy bazowej."""
    x = MERC_A * math.radians(lon) + MERC_B
    y = -MERC_C * math.log(math.tan(math.radians(45 + lat / 2))) + MERC_D
    return x, y


def _sciezki():
    tresc = BAZA.read_text(encoding='utf-8')
    znalezione = re.findall(r'<path d="([^"]+)"[^>]*stroke-width="([\d.]+)"', tresc)
    granice = [d for d, sw in znalezione if sw == '0.6']
    brzeg = [d for d, sw in znalezione if sw == '0.9']
    if len(brzeg) != 1:
        raise SystemExit(f'Oczekiwano jednej ścieżki linii brzegowej, jest {len(brzeg)}')
    return granice, brzeg[0]


def buduj(kadr, punkty, wyjscie, podpis, legenda='miejsce oznaczone numerem',
          pokaz_granice=True, roza=True):
    """kadr: (x, y, szerokość, wysokość) w układzie mapy bazowej.
    punkty: lista (lon, lat, etykieta, przesunięcie_etykiety)."""
    x0, y0, szer, wys = kadr
    granice, brzeg = _sciezki()
    skala = szer / 800.0  # grubości i promienie skalujemy do rozmiaru kadru

    czesci = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0} {y0} {szer} {wys}" '
        f'width="{szer}" height="{wys}">',
        f'  <title>{podpis}</title>',
        f'  <rect x="{x0}" y="{y0}" width="{szer}" height="{wys}" fill="{KOLOR_MORZA}"/>',
        f'  <path d="{brzeg}" fill="{KOLOR_LADU}" fill-rule="evenodd" stroke="none"/>',
    ]
    if pokaz_granice:
        czesci.append(f'  <g fill="none" stroke="{KOLOR_GRANIC}" '
                      f'stroke-width="{1.1 * skala:.2f}" stroke-linejoin="round">')
        czesci += [f'    <path d="{d}"/>' for d in granice]
        czesci.append('  </g>')
    czesci.append(f'  <path d="{brzeg}" fill="none" stroke="{KOLOR_BRZEGU}" '
                  f'stroke-width="{2.0 * skala:.2f}" stroke-linejoin="round"/>')

    r = 7.5 * skala
    for lon, lat, etykieta, (dx, dy) in punkty:
        x, y = na_piksele(lon, lat)
        if not (x0 <= x <= x0 + szer and y0 <= y <= y0 + wys):
            raise SystemExit(f'Punkt {etykieta} ({lon}, {lat}) wypada poza kadrem: '
                             f'({x:.0f}, {y:.0f})')
        czesci += [
            f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#ffffff" '
            f'stroke="#11181f" stroke-width="{2.2 * skala:.2f}"/>',
            f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r * 0.34:.1f}" fill="#11181f"/>',
            f'  <text x="{x + dx * skala:.1f}" y="{y + dy * skala:.1f}" '
            f'font-family="Arial,Helvetica,sans-serif" font-size="{26 * skala:.1f}" '
            f'font-weight="bold" fill="#11181f" stroke="#ffffff" '
            f'stroke-width="{4.5 * skala:.2f}" paint-order="stroke" '
            f'text-anchor="middle">{etykieta}</text>',
        ]

    if roza:
        rx, ry = x0 + szer - 46 * skala, y0 + 34 * skala
        dl = 30 * skala
        czesci += [
            f'  <line x1="{rx:.1f}" y1="{ry + dl:.1f}" x2="{rx:.1f}" y2="{ry:.1f}" '
            f'stroke="#11181f" stroke-width="{2.4 * skala:.2f}"/>',
            f'  <path d="M{rx:.1f},{ry - 4 * skala:.1f} l{-4.5 * skala:.1f},{9 * skala:.1f} '
            f'l{9 * skala:.1f},0 Z" fill="#11181f"/>',
            f'  <text x="{rx:.1f}" y="{ry + dl + 15 * skala:.1f}" '
            f'font-family="Arial,Helvetica,sans-serif" font-size="{20 * skala:.1f}" '
            f'font-weight="bold" fill="#11181f" text-anchor="middle">N</text>',
        ]

    # legenda w lewym dolnym rogu, na półprzezroczystym tle
    lw, lh = 268 * skala, 30 * skala
    lx, ly = x0 + 8 * skala, y0 + wys - lh - 8 * skala
    czesci += [
        f'  <rect x="{lx:.1f}" y="{ly:.1f}" width="{lw:.1f}" height="{lh:.1f}" '
        f'fill="#ffffff" fill-opacity="0.88" stroke="{KOLOR_BRZEGU}" '
        f'stroke-width="{1.0 * skala:.2f}"/>',
        f'  <circle cx="{lx + 15 * skala:.1f}" cy="{ly + lh / 2:.1f}" r="{r * 0.72:.1f}" '
        f'fill="#ffffff" stroke="#11181f" stroke-width="{1.8 * skala:.2f}"/>',
        f'  <circle cx="{lx + 15 * skala:.1f}" cy="{ly + lh / 2:.1f}" r="{r * 0.24:.1f}" '
        f'fill="#11181f"/>',
        f'  <text x="{lx + 28 * skala:.1f}" y="{ly + lh / 2 + 6 * skala:.1f}" '
        f'font-family="Arial,Helvetica,sans-serif" font-size="{17 * skala:.1f}" '
        f'fill="#11181f">{legenda}</text>',
        '</svg>',
    ]
    pathlib.Path(wyjscie).write_text('\n'.join(czesci), encoding='utf-8')
    print(f'Zapisano {wyjscie} — kadr {kadr}, punktów: {len(punkty)}')
    for lon, lat, etykieta, _ in punkty:
        x, y = na_piksele(lon, lat)
        print(f'  {etykieta}: ({lon:8.4f}, {lat:7.4f}) -> ({x:7.1f}, {y:7.1f})')


if __name__ == '__main__':
    # Wariant H, zadanie — wojna trzynastoletnia (1454-1466): miasta Prus Krolewskich
    # i panstwa zakonnego. Numery celowo nie ida w kolejnosci opisow A-F (§4 specyfikacji).
    PUNKTY = [
        (18.6042, 53.0138, '1', (0, -18)),    # Torun      -> opis C
        (20.5030, 54.7104, '2', (0, -18)),    # Krolewiec  -> opis E
        (19.0272, 54.0396, '3', (0, 28)),     # Malbork    -> opis A
        (17.5578, 53.6971, '4', (0, -18)),    # Chojnice   -> opis D
        (18.6466, 54.3520, '5', (-22, -4)),   # Gdansk     -> opis B
    ]
    buduj(kadr=(877.75, 1212.2, 150, 115), punkty=PUNKTY,
          wyjscie=str(BAZA.parent / 'wojna_trzynastoletnia_wariant_H.svg'),
          podpis='Mapa konturowa Prus Krolewskich i panstwa zakonnego w czasie wojny trzynastoletniej',
          legenda='miejsce oznaczone numerem')
