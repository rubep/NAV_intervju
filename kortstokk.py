import json

class Kortstokk:

    def __init__(self, url:str):
        """En instans av Kortstokk-klassen tar ett parameter – en url med JSON-data. Konstruktøren kaller metoden
        get_parseJsonData og lagrer returobjektet i instansvariabelen 'kortstokk'.
        :param url: str
        :return: ingen returverdi
        """
        self.kortstokk = self.__get_parseJsonData(url)


    def __get_parseJsonData(self, url:str):
        """Metoden henter ut et http.client.HTTPResponse-objekt med urlopen(), leser og dekoder objektet og lagrer det
        i variabelen 'data' (JSON-array som str.). Metoden konverterer videre strengen til Python-representasjon (list)
        med json.loads().
        :param url: str
        :return: list
        """
        # importerer riktig versjon av urlopen:
        try:
            # Python 3 versjon:
            from urllib.request import urlopen
        except ImportError:
            # Python 2 versjon:
            from urllib2 import urlopen

        response = urlopen(url)
        data = response.read().decode("utf-8")
        return json.loads(data)


    def get_kort(self):
        """Metoden trekker ett kort fra toppen av kortstokken og returnerer kortet til kallstedet. Et kort er et
        element (dict.) i listen 'kortstokk' med nøklene 'suit' og 'element' med tilhørende verdier.
        Et kall på get_kort returnerer og fjerner kortet på index 0 i kortstokken.
        *Jeg tolker "toppen av kortstokken" som at spillerne henter ut fra pos. 0 fra arrayet.
        :return: dict.
        """
        try:
            return self.kortstokk.pop(0)
        except IndexError:
            # vi vil aldri komme helt til bunnen av kortstokken i Blackjack, men det kunne jo tenkes at kortstokken
            # skulle brukes i et annet spill og derfor forhindrer try-blokken at programmet stopper opp hvis spillerne
            # fortsetter å trekke kort.
            print("Kortstokken er tom!")
