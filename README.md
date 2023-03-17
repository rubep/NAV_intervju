<h1 align="center">KODEOPPGAVE 1 i NAV FORS</h1>

<p align="center">Oppsummering</p>


Jeg har løst Blackjack-oppgaven som er kodeoppgave 1 i NAV Fors, og jeg har brukt Python i besvarelsen min.
Oppgaven er et Blackjack-spill med to deltagere, Marit og Ruby. Jeg har løst oppgaven objektorientert med tre klasser:
Blackjack (en subklasse av klassen Spill), Kortstokk og Spiller. Spillet kjøres ved å kalle på hovedprogrammet 'main.py'. 
Spillet er ikke interaktivt, men Spiller-klassen trekker kort fra kortstokken etter automatiske kall fra Blackjack-klassen.

Spill er en superklasse som tar inn en Kortstokk. Her er tanken at Spill kan være mange forskjellige spill og at det de 
har til felles er at de benytter seg av en kortstokk. Subklassen Blackjack tar inn to spillere, i tillegg til kortstokken. 
Blackjack-klassen sitter på reglene som er spesifisert i oppgaveteksten. Spiller-klassen representerer en spiller og har 
spillerens navn, en referanse til hvilket spill hen spiller, spillerens hånd under spillet og spillerens poengsum. 
Her er tanken at et Spiller-objekt kan opprettes i forbindelse med flere forskjellige spill. Spillerne trekker kort som 
lagres på spillernes respektive hånd, men det er Blackjack-klassen som sitter på reglene og avgjør hvilken spiller som vinner. 

SPILLETS REGLER: https://navikt.github.io/fors-public/kodeoppgaver/oppgave1.html#/ 



### AVHENGIGHETER OG VERSJON:
#### VERSJON
Koden kjører med Python 3.9.12.

#### AVHENGIGHETER:
- json
- urllib.request (Python3)
- urllib2 (Python2)


## HVORDAN KJØRE PROGRAMMET:
For å kjøre scriptene, og da spille én runde med spillet, ha alle scriptene i samme mappe og kjør main.py fra terminalen:

>> python main.py

Da kjører hovedprogrammet som setter spillet i gang. Hver gang main.py kalles vil programmet restarte og generere et 
nytt spill.


## HVORDAN TESTE PROGRAMMET:
Jeg har skrevet noen veldig enkle tester, som på ingen måte er ment å være heldekkende, men de sjekker enkel 
funksjonalitet i klassene og at metodene grovt sett oppfører seg som de skal. For å kjøre testene:
>> pytest test.py

Godt spill :)

##### Ruby Paloma, 17/03/2023.
