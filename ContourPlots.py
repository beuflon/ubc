import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height])

start, stop, n_values = -8, 8, 800

x_vals = np.linspace(start, stop, n_values)
y_vals = np.linspace(start, stop, n_values)

X, Y = np.meshgrid(x_vals, y_vals)

def f(x,y):
    return np.sqrt(x**2 + y**2)
    
Z = f(X, Y)

contour = ax.contour(X, Y, Z)
ax.set_title("Contour plot")
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()

