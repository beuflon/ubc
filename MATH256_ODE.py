# Libraries used: numpy for functions, scipy.integrate for ode solver, matplotlib.pylot for plotting y(t)
import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definition / Format of first order ODE: ay'(t) + by(t) = c(t) 

# Function of dy/dt (or y')
def model(y, t):
    dydt = -y + 1
    return dydt

# Initial condition
y0 = 0

# Time points
t = np.linspace(0,5)

# Solve ODE
y = odeint(model, y0, t)

# Plot
plt.plot(t, y)
plt.title('Graph of y(t)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()