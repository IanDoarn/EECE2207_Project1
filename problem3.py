import matplotlib.pyplot as plt
import numpy as np
from math import pow, sqrt

# Range from 0 to 5 seconds
t_range = np.linspace(0, 5.0)

# Functions
X = lambda t: (52 * t) - 9 * pow(t, 2)
Y = lambda t: 125 - 5 * pow(t, 2)
Vx = lambda t: 52 - 18 * t
Vy = lambda t: -10 * t
V = lambda vx, vy: sqrt(pow(vx, 2) + pow(vy, 2))

# Calculate values of functions
fV = [V(Vx(t), Vy(t)) for t in t_range]
fX = [X(t) for t in t_range]
fY = [Y(t) for t in t_range]

# Get the minimum velocity
min_velocity = min([[V(Vx(t), Vy(t)), i] for i, t in enumerate(t_range)])
print("Minimum velocity is {d[0]} at t={d[1]}".format(d=min_velocity))

# Plot the parametric function
plt.plot(fX, fY, 'r')
plt.title('parametric curve of y and x as a function of time')
plt.ylabel('y(m)')
plt.xlabel('x(m)')
plt.show()
