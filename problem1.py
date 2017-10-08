import matplotlib.pyplot as plt
import numpy as np
from math import pow, e

# range of time from 0 to 20
t_range = np.linspace(0, 20)
# position
xt = lambda t: (-3 + 4 * t) * pow(e, -0.4 * t)
# velocity
vt = lambda t: -(1 / 5) * (-26 + 8 * t) * pow(e, -(2 / 5) * t)
# acceleration
at = lambda t: -(1 / 25) * (-92 + 16 * t) * pow(e, -(2 / 5) * t)

# Calculate values for each function
fxt = [xt(t) for t in t_range]
fvt = [vt(t) for t in t_range]
fat = [at(t) for t in t_range]

# Plot functions
plt.plot(fxt, 'r-d', fvt, 'b-o', fat, 'g-s')
plt.legend(['x(t)=(-3+4t)e^(-0.4t)',
            'v(t)=-(1/5)(-26+8t)e^(-(2/5)t)',
            'a(t)=-(1/25)(-92+16t)e^(-(2/5)t)'])
plt.show()
