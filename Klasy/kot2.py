class Zwierze:
    def __init__(self,nazwa, wiek, waga):
        self._nazwa = nazwa
        self.waga = waga
        self.wiek = wiek

    def podaj_dane(self):
        print(f'Jestem zwierzeciem {self._nazwa}, mam {self.wiek} lat i ważę {self.waga} kg')

class Slon(Zwierze):
    pass # definicja bez zadnych swoich kodoww tylko z dziedziczenia

class Lew(Zwierze):
    def __init__(self,):
        self.iloscKlow = 4


Dumbo = Slon('Slonik Dumbo', 400, 300)
#Dumbo.nazwa = "Slonik Dumbo"
#Dumbo.waga = 300
#Dumbo.wiek = 400

Simba = Lew() #on ma brak atrubutów wymuszanych mimo, ze klasa zwierze je ma. Dla slonia musimy podawac bo nie ma swojego selfa. W inicie ządamy co ma byc na wejsciu.
Simba.iloscKlow = 3
Simba._nazwa = "Simba"
Simba.wiek = 35
Simba.waga = 450

Zwierzak = Zwierze("fff", 400, 300)
print(f"{Zwierzak}")

Simba.podaj_dane()
Dumbo.podaj_dane()


class Papuga(Zwierze):
    def __init__(self, nazwa, dlg_skrzydel):
        self.iloscPior = 4000
        self.nazwa = nazwa
        self.dlg_skrzydel = dlg_skrzydel

class Hybryda(Lew, Papuga): # dziedziczeniee z kliku klas
    pass

hyb = Hybryda()
hyb.