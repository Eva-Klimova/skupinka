"""
pujcovnaOprava.py

Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů. V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

1 Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hodit metoda řetězců jménem replace().
2 Upravte váš program tak, aby jméno souboru k otevření dostal na příkazové řádce, abychom mohli takto zpracovávat výkazy z různých souborů, aniž bychom museli upravovat samotný kód programu.
"""
import sys

# nazev_souboru = str(sys.argv[1])
cesta = str(sys.argv[1])

# soubor = open(nazev_souboru, encoding ="utf8")     # nebo cesta C:\git...)
soubor = open(cesta, encoding = "utf8")              
# nepíšu r"cesta", ale jen cesta, protože to r znamená raw - aby Python věděl, že zpětné lomítko a další znak něco znamená
# příkazový řádek to ví sám :-)
radky = [radek for radek in soubor]
soubor.close()
print(radky)

print([radek.split(" ") for radek in radky])

cisla = [radek.split(" ")[1].strip() for radek in radky if radek != "\n"]
print(cisla)

cisla = [float(cislo.replace(",", ".")) for cislo in cisla]
print(cisla)

soucet_km = sum(cisla)
print(soucet_km)


