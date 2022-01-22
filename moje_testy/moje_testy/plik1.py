
#%%
import csv
from os import write
w = []
s = ''
with open("Z.csv", 'r') as f:
    r = csv.reader(f, delimiter=';')
    for row in r:
        #print(row)
        print(", ".join(row))

with open("Z.csv", 'r') as f:
    r = csv.reader(f, delimiter=';')
    for row in r:
        for column in row:
            #print(row)
            #print("".join(column))
            s = "".join(column)
            w.append(s)
            
            g = " ".join(w)
    print (g)
    print (w)
#%%
with open("st.csv", "w", newline='') as g:
    write = csv.writer(g, delimiter=';')
    write.writerow(['1', '2', '3'])
    write.writerow(['4', '5', '6'])
# %%
with open("st.csv", "a", newline='') as g:
    write = csv.writer(g, delimiter=';')
    write.writerow(['7', '8', '9'])
# %%
