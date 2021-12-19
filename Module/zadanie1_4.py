import datetime

t1 = datetime.datetime(2019, 1, 1)
t2 = datetime.datetime(2021, 9, 8)

print(t2-t1)

#zad 2

my_birthday = datetime.datetime(1969, 1, 2)

print(f"Od dnia urodzin minelo: {(datetime.datetime.today() - my_birthday).days}")



#zad 3

koniec = datetime.datetime(2022, 1, 1, 0, 0, 0) - datetime.datetime.today()

print(f"Do konca\n roku zostalo {koniec}")
print(r"Do konca\n roku zostalo")

end1 = datetime.datetime(2021, 12, 31)
now = datetime.datetime.today()

diff1 = (end1 - now)

print(f"czas do konca roku {diff1}")
print(f"czas do konca roku {str(diff1)[:17]}")



print('5\\6')
print(r'5\6')

#zad 4


przesunieta_data = datetime.datetime.now() + datetime.timedelta(days=31)
print(f"Za 31 dni będzie dzień: {przesunieta_data}")



#date_string = "21 June, 2018"
#c = datetime.time.strftime(date_string, "%d %B, %Y")
#print("ffffff {c}")