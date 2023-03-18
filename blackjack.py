from kortstokk import Kortstokk
from spiller import Spiller

class Spill:
    def __init__(self, kortstokk: Kortstokk):
        """En instans av Spill-klassen har én instansvariabel – en kortstokk.

        :param kortstokk: Kortstokk
        """
        self.kortstokk = kortstokk



class Blackjack(Spill):
    """
    Klassen Blackjack arver klassen Spill. Et Spill-objekt består kun av en kortstokk og ingen spillere, mens
    Blackjack-klassen i tillegg har to spillere knyttet til et objekt av klassen. Klassen har metoder som reflekterer
    Blackjack-spillets regler.
    """

    def __init__(self, kortstokk:Kortstokk):
        """Blackjack-klassen arver Spill-klassens konstruktør. I tillegg har konstruktøren to tomme instansvariabler
        som er spillerne som skal spille spillet. I denne opggaven er det begrenset til to spillere.

        :param kortstokk: Kortstokk
        """
        super().__init__(kortstokk)
        self.s1 = None
        self.s2 = None


    def spill(self, spiller1:Spiller, spiller2:Spiller):
        """Når metoden kalles fra et hovedprogram settes Blackjack-spillet i gang. De to Spiller-objektene som skal
        spille bestemmes fra hovedprogrammet og sendes inn som argumenter til metoden. Spillerne trekker to kort hver i
        denne metoden. Når spillerne har trukket ferdig kaller metoden på __beregnScore().

        :param spiller1: Spiller
        :param spiller2: Spiller
        :return: ingen returverdi.
        """
        self.s1 = spiller1
        self.s2 = spiller2

        print(f"{self.s1.get_name()} og {self.s2.get_name()} trekker kort:")
        # Spillerne trekker to kort hver:
        self.s1.trekk(2)
        self.s2.trekk(2)

        # Kaller på __beregnScore() for å sjekke poeng:
        self.__beregnScore()


    def deal(self, n:int):
        """Metoden trekker n ant. kort fra toppen av kortstokken ved å kalle på get_kort() i Kortstokk-objektet og
        sender ett og ett kort videre til metoden __translate().
        *NB! Metoden deal() ligger i Blackjack-klassen mens metoden trekk() ligger Spiller-klassen. Jeg syntes det ga
        mening at det er en spiller som utfører trekket, mens det er spillet som leverer ut kortene.

        :param n: int
        :return: yield'er dict.
        """
        for i in range(n):
            yield self.__translate(self.kortstokk.get_kort())


    def __translate(self, kort:dict):
        """Metoden tar ett kort (dict.) som parameter og konverterer informasjonen på dette kortet slik at den kan lagres
        i et Spiller-objekt. Spesifikt oversetter metoden angivelsen på kortet til ønsket representasjon av 'suit' og
        'value' (en konkatenering av langformen på kortet som str som legges til spillerens hånd) i tillegg til å
        returnere poengsummen som en int. Disse to verdiene returneres som en dict. der spillerens hånd er nøkkel og
        poengsummen er verdi.

        :param kort: dict.
        :return: dict.
        """
        value = kort.get("value")
        poeng = 0
        # Sjekker om poengsummen er et siffer eller en bokstav:
        try:
            poeng += int(value)
        except ValueError:
            if kort.get("value") == "A":
                poeng += 11
            else:
                poeng += 10

        # Returnerer en ordbok med spillerens hånd som nøkkel og poengsummen som verdi:
        return {kort.get("suit")[0] + kort.get("value") + ", ": poeng}


    def __beregnScore(self):
        """Metoden beregner poengsummen etter spillets første runde og skriver ut informasjon om utfallet til terminal.
        Dersom ingen spillere har fått 21 poeng kaller metoden på __fortsettSpillet() for å gå videre til neste runde.

        :return: ingen returverdi.
        """
        print("\nVi sjekker poengscore:")
        print(self.s1)
        print(self.s2)

        # Hvis ingen av spillerne har fått 21 poeng eller mer, så skal spillet fortsette:
        if self.s1.get_poeng() < 21 and self.s2.get_poeng() < 21:
            print("\nSpillet fortsetter! Trekk flere kort:")
            self.__fortsettSpillet()

        # Hvis begge spillerne fikk 21 poeng har vi en tie!:
        elif self.s1.get_poeng() == 21 and self.s2.get_poeng() == 21:
            print(f"\nSpillet ble uavgjort!\n{self.s1.get_hand()}\n{self.s2.get_hand()}")

        # Hvis spiller 1 har fått 21 poeng har spiller 1 vunnet:
        elif self.s1.get_poeng() == 21:
            print(f"\nVinner: {self.s1.get_name()}\n{self.s1.get_hand()}\n{self.s2.get_hand()}")

        # Hvis spiller 2 har fått 21 poeng har spiller 2 vunnet:
        elif self.s2.get_poeng() == 21:
            print(f"\nVinner: {self.s2.get_name()}\n{self.s1.get_hand()}\n{self.s2.get_hand()}")

        # Hvis én av spillerne har fått mer enn 21 poeng har denne spilleren fått to ess og tapt:
        elif self.s1.get_poeng() > 21:
            print(f"\nVinner: {self.s2.get_name()}\n{self.s1.get_hand()}\n{self.s2.get_hand()}")

        else:
            print(f"\nVinner: {self.s1.get_name()}\n{self.s1.get_hand()}\n{self.s2.get_hand()}")


    def __fortsettSpillet(self):
        """Metoden kalles kun dersom ingen av spillerne fikk 21 poeng eller mer i første runde. Spiller 1 trekker kort
        frem til hen har minst 17 poeng. Får spilleren mer enn 21 poeng, har spilleren tapt. Får spilleren 21 pong eller
        mindre trekker spiller 2 kort frem til hen har flere poeng enn spiller 1. Får spiller 2 mer enn 21 poeng har
        spiller 2 tapt.

        :return: ingen returverdi.
        """
        # Jeg tolker oppgaveteksten slik at at spiller 1 skal trekke kort for å starte runde 2 selvom de to første
        # kortene fra runde 1 utgjør mer enn 17 poeng:
        self.s1.trekk()
        # Deretter fortsetter spiller 1 å trekke så lenge poengsummen er lavere enn 17:
        while self.s1.get_poeng() < 17:
            self.s1.trekk()

        # Dersom spiller 1 ender opp med mer enn 21 poeng har spilleren tapt:
        if self.s1.get_poeng() > 21:
            print(f"\n{self.s1.get_name()} fikk mer enn 21 poeng!")
            print(f"\nVinner: {self.s2.get_name()}\n{self.s1.get_hand()}\n{self.s2.get_hand()}")

        # Hvis ikke skal spiller 2 trekke frem til poengummen er høyere enn spiller 1 sin poengsum:
        else:
            while self.s2.get_poeng() <= self.s1.get_poeng():
                self.s2.trekk()

            # Hvis spiller 2 får mer enn 21 poeng har spiller 1 vunnet.
            if self.s2.get_poeng() > 21:
                print(f"\nVinner: {self.s1.get_name()}\n{self.s1.get_hand()}\n{self.s2.get_hand()}")
            # Hvis spiller 2 får 21 poeng eller mindre har spiller 1 vunnet:
            else:
                print(f"\nVinner: {self.s2.get_name()}\n{self.s1.get_hand()}\n{self.s2.get_hand()}")



