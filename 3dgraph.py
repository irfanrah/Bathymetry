import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time
import numpy
import random

count=0
count2=0
fig = plt.figure()
ax = fig.gca(projection='3d')
z = [0]
x = [0]
y = [0]

plt.ion()    ###

plt.show()
while True:
	count +=1
	for sby in range(0,10):
		for sbx in range(0,10):
			
			x.append(sbx)
			y.append(sby) #
			dataz = random.randrange(0, 4,1)
			z.append(dataz/4) # just for eye-candy
			ax.plot(numpy.array(x),numpy.array(y),numpy.array(z))
			ax.scatter(numpy.array(x),numpy.array(y),numpy.array(z))
			plt.pause(1)
			plt.draw()
			count2 +=1
