# początki tworzenia klas

from typing import List


# class MojaKlasa:
#     def wyswietl():
#         return 'Witaj świecie'

# x = MojaKlasa
# print(x.wyswietl())

class Prosotopadloscian:
    def __init__(self): # konstruktor klasy. Standardowo wstawiamy tu wlasciwosci ktore beda uzywane
        self.podstawa_a = 0 #wlasciwosci instancyjne - sel. inne dla kazdej instancji
        self.podstawa_b = 0
        self.wysokosc_h = 0
    
    
    def objetosc(self):
        return (self.podstawa_a * self.podstawa_b * self.wysokosc_h)

    def malowanie(self):
        return 2 * ((self.podstawa_a * self.wysokosc_h) + (self.podstawa_b * self.wysokosc_h))


WTC=Prosotopadloscian()
WTC.podstawa_a = 100
WTC.podstawa_b = 200
WTC.wysokosc_h = 400

print(WTC.objetosc())

print(WTC.malowanie())


class Szopa:
    def __init__(self, bok_a, bok_b, wys_h): # konstruktor klasy. i tu sa zmiene lokalne ktore przychodza z zewnatrz
        self.podstawa_a = bok_a
        self.podstawa_b = bok_b
        self.wysokosc_h = wys_h
        
    
    
    def malowanie(self):
        return 2 * ((self.podstawa_a * self.wysokosc_h) + (self.podstawa_b * self.wysokosc_h))


szopa1 = Szopa(2,3,5)
print(szopa1.malowanie())
szopa2 = Szopa(5,6,7)
print(szopa2.malowanie())
for i in range (1, 10):
    szopa3 = Szopa(i,i+1,i+2)
    print(szopa3.malowanie())