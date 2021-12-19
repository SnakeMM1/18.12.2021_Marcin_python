
#%%
import matplotlib.pyplot as plt
import csv


file_name = 'month.csv'

with open (file_name) as file:
    reader = csv.reader(file)
    header1 = next(reader) # next pobiera pierwsza linie

print(header1)
# %%
