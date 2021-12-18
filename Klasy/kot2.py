class Zwierze:
    def __init__(self,nazwa, wiek, waga):
        self.nazwa = nazwa
        self.waga = waga
        self.wiek = wiek

    def podaj_dane(self):
        print(f'Jestem zwierzeciem {self.nazwa}, mam {self.wiek} lat i ważę {self.waga} kg')

class Slon(Zwierze):
    pass # definicja bez zadnych swoich kodoww tylko z dziedziczenia

class Lew(Zwierze):
    def __init__(self,):
        self.iloscKlow = 4


