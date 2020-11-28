import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

min_x, max_x, dim_x = (-10, 10, 100)
min_y, max_y, dim_y = (-10, 10, 100)


def gen_fake_data():
    # First we generate the (x,y,z) tuples to imitate "real" data
    # Half of this will be in the + direction, half will be in the - dir.
    xy_max_error = 0.2

    # Generate the "real" x,y vectors
    x = np.linspace(min_x, max_x, dim_x)
    y = np.linspace(min_y, max_y, dim_y)

    # Apply an error to x,y
    x_err = (np.random.rand(*x.shape) - 0.5) * xy_max_error
    y_err = (np.random.rand(*y.shape) - 0.5) * xy_max_error
    x *= (1 + x_err)
    y *= (1 + y_err)

    # Generate fake z
    rows = []
    for ix in x:
        for iy in y:
            z = math.sqrt(ix**2 + iy**2)
            rows.append([ix,iy,z])

    mat = np.array(rows)
    return mat
    
def method_2():
    mat = gen_fake_data()

    x = np.linspace(min_x, max_x, dim_x)
    y = np.linspace(min_y, max_y, dim_y)

    X,Y = np.meshgrid(x, y)

    # Interpolate (x,y,z) points [mat] over a normal (x,y) grid [X,Y]
    #   Depending on your "error", you may be able to use other methods
    Z = interpolate.griddata((mat[:,0], mat[:,1]), mat[:,2], (X,Y), method='nearest')
    #ax2.pcolormesh(X,Y,Z)
    surf = ax.plot_surface(X, Y, Z)
    plt.show()
def func(x, y):
	return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2
    

points = np.random.rand(10, 2)
values = func(points[:3], points[:1])
print("poin ", points," val ",values)
