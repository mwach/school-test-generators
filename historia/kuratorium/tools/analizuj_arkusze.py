#!/usr/bin/env python3
"""Zestawia parametry archiwalnych arkuszy konkursowych na podstawie warstwy tekstowej.

Punktacja w arkuszach powtarza się (raz przy zadaniu, raz w karcie odpowiedzi),
dlatego maksimum punktów liczone jest osobno dla każdego numeru zadania.
"""

import pathlib
import re
import sys

ROMAN = r"(?=[IVX])X{0,3}(?:IX|IV|V?I{0,3})"
# Arkusze zapisują punktację jako "ZADANIE VII (0 – 5 p.)" albo "Zadanie 7 (0 – 5 punktów)".
ZADANIE_Z_PUNKTAMI = re.compile(
    rf"ZADANIE\s+({ROMAN}|\d{{1,2}})\b[^\n(]{{0,40}}\(\s*0\s*[–—-]\s*(\d{{1,2}})\s*(?:p|pkt|punkt)",
    re.IGNORECASE,
)
# Klucze z ostatnich lat używają tabeli "Nr zadania | Liczba punktów", np. "I 0-10".
KLUCZ_TABELA = re.compile(rf"\b({ROMAN})\s+0\s*[-–—]\s*(\d{{1,2}})\b")
ZADANIE = re.compile(rf"ZADANIE\s+({ROMAN}|\d{{1,2}})\b", re.IGNORECASE)
DEKLARACJA = re.compile(
    r"składa się z\s+(\d+)\s+stron[^.]*?zawiera\s+(\d+)\s+zada", re.IGNORECASE | re.DOTALL
)
CZAS = re.compile(r"(\d{2,3})\s*minut", re.IGNORECASE)


def etap(nazwa: str) -> str:
    lowered = nazwa.lower()
    if "wojewodzki" in lowered:
        return "wojewódzki"
    if "rejon" in lowered:
        return "rejonowy"
    if "szkolny" in lowered:
        return "szkolny"
    return "?"


def main() -> int:
    katalog = pathlib.Path(sys.argv[1])
    naglowek = (
        f"{'plik':<38}{'etap':<12}{'typ':<8}{'zadań':>6}{'pkt':>6}"
        f"{'deklarowane':>14}{'czas':>9}"
    )
    print(naglowek)
    print("-" * len(naglowek))
    for plik in sorted(katalog.glob("*.txt")):
        tekst = plik.read_text(encoding="utf-8")
        punkty: dict[str, int] = {}
        for numer, wartosc in ZADANIE_Z_PUNKTAMI.findall(tekst):
            klucz = numer.upper()
            punkty[klucz] = max(punkty.get(klucz, 0), int(wartosc))
        if not punkty:
            for numer, wartosc in KLUCZ_TABELA.findall(tekst):
                if numer:
                    punkty[numer.upper()] = max(punkty.get(numer.upper(), 0), int(wartosc))
        numery = {m.group(1).upper() for m in ZADANIE.finditer(tekst) if m.group(1)}
        deklaracja = DEKLARACJA.search(tekst)
        czas = CZAS.search(tekst)
        opis = f"{deklaracja.group(2)} zad./{deklaracja.group(1)} s." if deklaracja else "-"
        print(
            f"{plik.stem:<38}{etap(plik.stem):<12}"
            f"{'klucz' if plik.stem.endswith('-k') else 'arkusz':<8}"
            f"{len(numery) or len(punkty):>6}{sum(punkty.values()) or '-':>6}"
            f"{opis:>14}{(czas.group(1) + ' min') if czas else '-':>9}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
