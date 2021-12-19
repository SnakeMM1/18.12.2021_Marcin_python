import datetime

t1 = datetime.datetime(2019, 1, 1)
t2 = datetime.datetime(2021, 9, 8)

print(t2-t1)

#zad 2

my_birthday = datetime.datetime(1969, 1, 2)

print(f"Od dnia urodzin minelo: {datetime.datetime.today() - my_birthday}")



#zad 3

koniec = datetime.datetime(2022, 1, 1, 0, 0, 0) - datetime.datetime.today()

print(f"Do konca roku zostalo {koniec}")


#zad 4


przesunieta_data = datetime.datetime.today() + datetime.timedelta(days=31)
print(f"Za 31 dni będzie dzień: {przesunieta_data}")


