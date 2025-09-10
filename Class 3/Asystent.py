class Asystent:
    def __init__(self, nazwa, wersja):
        self.nazwa = nazwa
        self.wersja = wersja


class AnalizaJezykowa:
    def analizuj_zapytanie(self, zapytanie):
        zapytanie = zapytanie.lower()
        if "pogoda" in zapytanie:
            return "pogoda"
        elif "cześć" in zapytanie or "hej" in zapytanie:
            return "powitanie"
        else:
            return "ogólna"


class GeneratorOdpowiedzi:
    def generuj_odpowiedz(self, analiza):
        if analiza == "pogoda":
            return "Dzisiaj jest słonecznie."
        elif analiza == "powitanie":
            return "Witaj, jak mogę Ci pomóc?"
        else:
            return "Nie jestem pewien, jak odpowiedzieć."


class InteligentnyAsystent(Asystent):
    def __init__(self, nazwa, wersja):
        super().__init__(nazwa, wersja)
        self.analiza = AnalizaJezykowa()
        self.generator = GeneratorOdpowiedzi()

    def odpowiadaj(self, zapytanie):
        wynik_analizy = self.analiza.analizuj_zapytanie(zapytanie)
        odpowiedz = self.generator.generuj_odpowiedz(wynik_analizy)
        return odpowiedz


if __name__ == "__main__":
    asystent = InteligentnyAsystent("SmartAssistant", "1.0")
    zapytanie = "Cześć, jaka jest pogoda dzisiaj?"
    odpowiedz = asystent.odpowiadaj(zapytanie)
    print(f"Zapytanie: {zapytanie}")
    print(f"Odpowiedź: {odpowiedz}")
