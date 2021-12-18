# początki tworzenia klas

from typing import List
from kot import KOT

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

    Pomalowanebud = 0
    def __init__(self, bok_a, bok_b, wys_h): # konstruktor klasy. i tu sa zmiene lokalne ktore przychodza z zewnatrz
        self.podstawa_a = bok_a
        self.podstawa_b = bok_b
        self.wysokosc_h = wys_h
        Szopa.Pomalowanebud+=1  #ile razy inicjujemy nowy obiekt licznik sie nam zwieksza i wiemy ile budynkow mozemy pomalowac (ile razy robilismy obliczenia)
     


    def malowanie(self):
        X=+ 1
        return 2 * ((self.podstawa_a * self.wysokosc_h) + (self.podstawa_b * self.wysokosc_h))
        
   
        

X = 0       
# szopa1 = Szopa(2,3,5)
# print(szopa1.malowanie())
# szopa2 = Szopa(5,6,7)
# print(szopa2.malowanie())
for i in range (1, 10):
    szopa3 = Szopa(i,i+1,i+2)
    print(szopa3.malowanie())
    ilosc_calk_metrow_do_pomalowania =+ szopa3.malowanie()
    print(Szopa.Pomalowanebud)
print(ilosc_calk_metrow_do_pomalowania)   

Garfield = KOT()
Garfield.wiek = 12
print(Garfield.miauczenie())