import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, pow, sin

y_vector = np.linspace(20, 48)

pythagorian_theorem = lambda a, b: sqrt(pow(a, 2) + pow(b, 2))
snells_law = lambda th, a, vrun, vswim: sin(th) / sin(a) == vrun / vswim

v_run = 3 # meter / second
v_swim = 1 # meter / second
L = 48 # meters
d_s = 30 # meters
d_w = 42 # meters
d_sw = d_s + d_w
A = pythagorian_theorem(L, d_sw)
B = pythagorian_theorem(L, d_s)