import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin

# 0 ≤ t ≤ 4π, 1000 points to ensure nice curved lines
t_range = np.linspace(0, 4 * pi, num=1000)

X = lambda t: (13 * cos(t)) - 2 * (cos(6.5 * t))
Y = lambda t: (13 * sin(t)) - 2 * (sin(6.5 * t))

fX = [X(t) for t in t_range]
fY = [Y(t) for t in t_range]

plt.plot(fX, fY, 'r')
plt.show()
