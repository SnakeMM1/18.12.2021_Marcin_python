

class zwierze:
    def __init__(self):
        self.name = " "
        self.kolor_oczu = ''
        self.kolor_siersci = ''
        self.dlugosc = 0
        self.wysokosc = 0
        self.wiek = 0
        self.waga = 0
    
    def jedzenie(self):
        self.waga += 10
        print(f"{self.name} jest coraz grubszy. Wazy {self.waga}")

zwierz1 = zwierze()
zwierz1.name = "Kot1"
zwierz1.kolor_oczu = "brąz"
zwierz1.waga = 6

zwierz1.jedzenie()
print(zwierz1.name)

