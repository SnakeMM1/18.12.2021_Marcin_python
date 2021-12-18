class Pojazd_mech:
    def __init__(self):
        self.nazwa = " "
        self.Sluzbowy = " "
        self.ilosc_kol = 0
    
class Auto(Pojazd_mech):
    def __init__(self):
        ilosc_kol = 4
        self.rodzaj = " "

class Motor(Pojazd_mech):
    def __init__(self):
        self.typ = " "
        ilosc_kol = 2

motor1 = Motor()
auto1 = Auto()
motor1.typ = "Enduro"
auto1.rodzaj = "Sedan"

print(f'{motor1.typ}')
print(f"{auto1.rodzaj}")

auto1.ilosc_kol = 6
print(f'{auto1.ilosc_kol}')

#motor1.ilosc_kol = 6
print(f'{motor1.ilosc_kol}')