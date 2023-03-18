class Spiller:

    def __init__(self, name:str, spill):
        """En instans av Spiller-klassen tar to parametere – et navn og et spill. I tillegg oppretter konstruktøren
        to instansvarialer – spillerens hånd og poengsum.

        :param name: str
        :param spill: any (vil være Blackjack i vårt tilfelle)
        """
        self.name = name
        self.spill = spill

        self.hand = ""
        self.poeng = 0


    def get_poeng(self):
        """Returnerer spillerens poengsum.

        :return: int
        """
        return self.poeng


    def get_name(self):
        """Returnerer spillerens navn.

        :return: str
        """
        return self.name


    def get_hand(self):
        """Returnerer en string med spillerens resultat i riktig representasjon når spillet er slutt.

        :return: str
        """
        return f"{self.name} | {self.poeng} | {self.hand[:-2]}" #fjerner komma og mellomrom på slutten med -2.


    def trekk(self, n=1):
        """Metoden tar ett argument (n, ant. kort å trekke med 1 som default). Spilleren trekker n antall kort ved å
        kalle på metoden deal() i det spillet spilleren er knyttet til. Metoden deal() returnerer alle kortene spilleren
        har trukket i dict. (én og én) og de lagres som en liste i variabelen 'kort'. Deretter hentes informasjonen ut
        fra listen med en for-løkke og spillerens hånd og poengsum oppdateres. Til slutt kaller metoden __visKort().

        :param n: int (default = 1)
        :return: ingen returverdi.
        """
        # Spilleren gjør trekker n ant. kort via spillet:
        kort = list(self.spill.deal(n))

        for k in kort:
            for suit, value in k.items():
                self.hand += suit
                self.poeng += value
                # Kaller på __visKort() å skrive ut informasjonen på kortet som ble trukket til terminal:
                self.__visKort(k)


    def __visKort(self, kort):
        """Metoden skriver ut kortinformasjon til terminal.

        :param kort: dict.
        :return: ingen returverdi.
        """
        print(self.name + " trakk " + next(iter(kort))[:-2]) #fjerner komma og mellomrom på slutten med -2.

    def __str__(self):
        """String-representasjon av objektet. Returnerer en string med navn på Spilleren og poengsum.

        :return: str
        """
        return f"{self.name} har {self.poeng} poeng"



