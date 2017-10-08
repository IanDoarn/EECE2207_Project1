import matplotlib.pyplot as plt
import numpy as np
from math import pow, e

# Create range of points
vd_range = np.linspace(1.0, 5.0, num=100)

# create functions for both ideal equations
iD_1 = lambda I, kTq, vD: I * (pow(e, kTq * vD) - 1)
iD_2 = lambda vS, vD, R: (vS - vD) / R

# Initial values
I_0 = pow(10, -14) # Amps
v_S = 1.5 # Volts
r = 1200 # Ohms
kT_q = 30 # Milli Volts

# Calculate values
fiD_1 = [iD_1(I_0, kT_q, v) for v in vd_range]
fiD_2 = [iD_2(v_S, v, r) for v in vd_range]

plt.plot(fiD_1, 'r', fiD_2, 'b')
plt.legend(['Io * (e^(qvD/kT) - 1)', '(vS - vD) / R'])
plt.show()
