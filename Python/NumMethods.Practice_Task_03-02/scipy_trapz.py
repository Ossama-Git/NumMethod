from numpy import *
from scipy.integrate import trapz
import matplotlib.pyplot as plt
import math


def f(x):
    return math.pow(x, 2) * math.cos(x)

a = 0
b = math.pi * 2
n =300
h = (b - a) / n

x = arange(a, b + h, h)
#print(x)

y = []
for xi in x:
    y.append(f(xi))

#print(y)

I = trapz(y, x=x)
print(I)

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x, y, 'r')
plt.show()