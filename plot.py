from mpl_toolkits import mplot3d

import cmath
import sys
import numpy as np
import matplotlib.pyplot as plt

def realBinet (n):
    return ((((1+cmath.sqrt(5))/2)**n - ((1-cmath.sqrt(5))/2)**n)/cmath.sqrt(5)).real

def imagBinet (n):
    return ((((1+cmath.sqrt(5))/2)**n - ((1-cmath.sqrt(5))/2)**n)/cmath.sqrt(5)).imag

if len(sys.argv) == 3:
    min = float(sys.argv[1])
else:
    min = 0

if len(sys.argv) == 3:
    max = float(sys.argv[2])
else:
    max =  5

fig = plt.figure()
ax = plt.axes(projection="3d")

x_line = np.linspace(min, max, 1000)
y_line = list(map(realBinet,x_line))
z_line = list(map(imagBinet,x_line))
ax.plot3D(x_line, y_line, z_line)


plt.show()
