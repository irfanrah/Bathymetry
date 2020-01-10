import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time
import numpy as np
import random
from matplotlib import cm

count=0
count2=0
fig = plt.figure()
ax = fig.gca(projection='3d')
plt.ion()    ###
x = [0, 8]
y = [0, 8]
Z = np.zeros(shape=(32,32))
plt.show()
while True:
	count +=1
	for sby in range(-5, 5):
		for sbx in range(-5, 5):
			
			dataz = random.randrange(5)
			x_a = np.arange(min(x), max(x), 0.25)
			y_a = np.arange(min(y), max(y), 0.25)
			X, Y = np.meshgrid(x_a, y_a)
			x_shape = X.shape
			print(x_shape)
			if Z.shape != X.shape:
				print(Z.shape)
				if X.shape[0] > Z.shape[0]:
					#print(X.shape)
					#print(Z.shape)
					#print(np.zeros(shape=X.shape[0]).shape)
					Z = np.append(Z, [np.zeros(5)], axis=0)
				# if X.shape[1] > Z.shape[1]:
					#Z = np.append(Z, [np.zeros(shape=Z.shape[1])], axis=1)		
			# print(X)
			# print(Y)
			Z[sby,sbx] = dataz
			# Z = np.ones(shape=X.shape)
			# for index, z_val in enumerate(z):
			#	 Z[x[index], y[index]] = z_val
			surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
			# ax.plot(np.array(x),np.array(y),np.array(z))
			# ax.scatter(np.array(x),np.array(y),np.array(z))
			plt.pause(1)
			plt.draw()
			count2 +=1
