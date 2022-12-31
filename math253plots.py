from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt 
import sklearn
#Define function

def f(x,y):
    return x**2*y+y**3-27*y

#  3D plots
fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.arange(-10, 10, 0.2)
y = np.arange(-10, 10, 0.2)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax.contour3D(X,Y,Z, 50, cmap = 'rainbow')
ax.set_title('3D plot')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()
