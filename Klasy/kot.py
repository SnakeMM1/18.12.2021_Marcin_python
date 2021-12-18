class KOT:

    def __init__(self):
        self.name = " "
        self.kolor_oczu = ''
        self.kolor_siersci = ''
        self.dlugosc = 0
        self.wysokosc = 0
        self.wiek = 0
        self.waga = 0
    
    def miauczenie(self):
        if self.wiek > 10:
            return 'Kot spi ponad 10 h'
        else: return 'Kot spi mniej niz 10 h'

    def jedzenie(self):
        self.waga += 10
        print(f"Kot jest coraz grubszy. Wazy {self.waga}")
         
        
kot1 = KOT()

kot1.wiek = 12
print(kot1.miauczenie())
print(kot1.wiek)

kot1.wiek = 9
print(kot1.miauczenie())
print(kot1.wiek)

kot1.waga = 10
kot1.jedzenie()
#print(kot1.waga)
kot1.jedzenie()
#print(kot1.waga)
kot1.jedzenie()
#

print((KOT))