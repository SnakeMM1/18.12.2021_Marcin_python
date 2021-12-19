#%%

import matplotlib.pyplot as plt
import numpy as np


x_values = list(range(-11, 11, 2))
y_values = [(x ** 2 ) for x in x_values]
y_values1 = [(x ** 3)/(5*x+x) for x in x_values]


fig, ax = plt.subplots() # zmienna reprezentujaca nasz rysunek
#fig, ax1 = plt.subplots()

ax .plot(x_values, y_values, c='red', linewidth=3)
ax .plot(x_values, y_values1, c='blue', linewidth=3)
ax.set_title('Kwadraty liczb', fontsize = 20)
ax.set_xlabel('Liczby', fontsize = 16)
ax.set_ylabel('Kwadraty', fontsize = 16)

# ax1 .plot(x_values, y_values1, c='red', linewidth=3)
# ax1.set_title('Kwadraty liczb', fontsize = 20)
# ax1.set_xlabel('Liczby', fontsize = 16)
# ax1.set_ylabel('Kwadraty', fontsize = 16)


plt.show()