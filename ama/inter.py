from scipy import interpolate
import random
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [422,424,424,422,422,421,421,425,421,424]
y = [87,96,87,87,83,93,85,88,86,91]
z = [92.73,94.88,92.92,92.73,92.04,93.92,92.24,93.23,92.42,93.78]

xv = np.linspace(min(x), max(x), 20)
yv = np.linspace(min(y), max(y), 20)
[X,Y] = np.meshgrid(xv, yv)

dot = np.column_stack((x,y))
Z = interpolate.griddata(dot,z,X,Y,method='nearest')




surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.show()
