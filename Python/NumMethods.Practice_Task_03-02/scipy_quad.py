import scipy
import math
from scipy.integrate import quad

def f(x):
    return math.pow(x, 2) * math.cos(x)

# quad() is a function that calculate definite integrals.
# It returns an evaluated value of the integral and estimated absolute error.
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html
I = quad(f, 0, math.pi * 2)

# The output contains the value of the definite integral and the estimated precision
print(I)