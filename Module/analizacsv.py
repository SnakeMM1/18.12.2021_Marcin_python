
#%%
import matplotlib.pyplot as plt
import csv
# code
# 
#import datetime
from datetime import datetime


file_name = 'month.csv'

with open (file_name) as file:
    reader = csv.reader(file)
    header1 = next(reader) # next pobiera pierwsza linie, nastepny nest pobiera nastepna linie

# print(header1)
# for index, column_header in enumerate(header1): # numery kolejnych naglowkow ktorych mamy 6. Dodaje numery
#     print(index, column_header)

# for column_header in header1: # dla porownania co daje bez enumerate
#     print(column_header)

    highs =[]
    dates = []
    lows = []

    for row in reader:
        high = int(row[5])
        date = datetime.strptime(row[2], '%Y-%m-%d') # nawias kwadratowy oznacza odczyt z 5 kolumny. indeksy przekazujemy w nawiasach kwadratowych.
        low = int(row[6])
        highs.append(high)
        dates.append(date)
        lows.append(low)

print(highs)
print(dates)


fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', label='highs')
ax.plot(dates, lows, color='blue', label='lows') #drugi wykres

ax.set_title ('Najw temp w lipcu')
ax.set_ylabel('Temp w F')

fig.autofmt_xdate() #upakowanie dat podpisu pod katem
ax.legend()

plt.show() # uruchamia rysowanie wykresu na ekranie
#plt.savefig('temp.png') # zapisuje plik png. Ale albo show albo savefig
# %%
