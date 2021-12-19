import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-2,2,1000)
y = np.linspace(-1,1,1000)
x_axis = []
y_axis = []


def mandel_set(x,y):
    for i in x:
     for z in y:
        a = complex(i +z*((-1)**(-1/2)))
        m = mandel(a)
        if abs(m) < 2:
            x_axis.append(i)
            y_axis.append(z)

def mandel(c):
    z = 0
    for i in range(0,10):
        z = z**2 + c
    return z


mandel_set(x,y)
plt.scatter(x,y)