from kortstokk import Kortstokk
from spiller import Spiller
from blackjack import Blackjack

url = "https://blackjack.labs.nais.io/shuffle"

def testKortstokk():
    """Tester Kortstokk-klassen: Ikke heldekkende, men enkle tester for å sjekke at det går å hente ut en kortstokk og
    at to kortstokker ikke er like. I tillegg sjekkes get_Kort-metoden.

    :return: ingen returverdi.
    """
    k1 = Kortstokk(url)
    k2 = Kortstokk(url)

    # Sjekker at kortstokkene ikke er like:
    assert k1.kortstokk != k2.kortstokk

    # Sjekker at lengden på kortstokk-listen er redusert med 1 etter ett trekk fra k1:
    k1.get_kort()
    assert len(k1.kortstokk) == 51
    # Sjekker at det ikke er trukket kort fra k2:
    assert len(k2.kortstokk) == 52

    # Sjekker at hvis en kortstokk tømmes, så returneres None:
    i = 0
    while i < len(k2.kortstokk):
        k2.get_kort()

    assert len(k2.kortstokk) == 0

    assert k2.get_kort() == None


def testSpiller():
    """Tester Spiller-klassen: Tester at enkelte funksjoner i Spiller-klassen fungerer som de skal.

    :return: ingen returverdi.
    """
    # Lager en kortstokk, et spill, og en spiller:
    k = Kortstokk(url)
    spill = Blackjack(k)
    testSpiller = Spiller("Test", spill)

    # Sjekker ant. poeng før start:
    assert testSpiller.get_poeng() == 0

    # Sjekker spillerens navn:
    assert testSpiller.get_name() == "Test"

    # Sjekker at hånden er tom før spilleren har trukket kort:
    assert len(testSpiller.hand) == 0

    # Sjekker at et trekk fra kortstokken fungerer:
    testSpiller.trekk()

    # Sjekker lengden på kortstokken etter trekk:
    assert len(k.kortstokk) == 51

    # Sjekker at hånden ikke lenger er tom:
    assert len(testSpiller.hand) > 0

    # Sjekker at spilleren har fått noen poeng:
    assert testSpiller.get_poeng() > 0


def testSpillet():
    """Tester Blackjack-klassen: Tester at enkelte funksjoner i Blackjack-klassen fungerer som de skal.

    :return: ingen returverdi.
    """
    # Jeg ønsker å kjøre en rekke tester for å ha kontrollert flere utfall av spillet:
    kort = [Kortstokk(url) for _ in range(50)]
    # Kontrollerer at jeg fikk 50 Kortstokker
    assert len(kort) == 50 and type(kort[0]) == Kortstokk

    # Lager og starter 50 spill med to spillere:
    for i in range(len(kort)):
        spill = Blackjack(kort[i])
        ts1 = Spiller("Test 1", spill)
        ts2 = Spiller("Test 2", spill)

        # Starter hvert spill:
        spill.spill(ts1, ts2)

        # Sjekker at begge spillerne har fått poeng:
        assert ts1.get_poeng() > 0
        assert ts2.get_poeng() > 0

        # Sjekker at 4 eller flere kort er trukket fra kortstokken:
        assert len(kort[i].kortstokk) <= 48

        # SJEKKER VINNER_EVALUERINGEN:
        # Hvis spiller 1 har mindre enn 17 poeng ved spillets slutt, da fikk spiller 2 21 poeng i første runde:
        if ts1.get_poeng() < 17:
            assert ts2.get_poeng() == 21

        # Hvis spiller 1 har fått mer enn 21 poeng, da har spiller 2 21 poeng eller lavere:
        elif ts1.get_poeng() > 21:
            assert ts2.get_poeng() <= 21

        # Og omvendt:
        elif ts2.get_poeng() > 21:
            assert ts1.get_poeng() <= 21





