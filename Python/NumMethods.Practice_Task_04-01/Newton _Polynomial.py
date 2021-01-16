from matplotlib import pyplot as plt

#data points
x = [1.0, 2.0, 2.5, 3.0, 5.0]
y = [1.2, 3.1, 4.0, 2.1, 1.0]

def diff(i, k, x, y):
    if k == 0:
        return y[i]
    elif k == 1:
        return (y[i + 1] - y[i]) / (x[i + 1] - x[i])
    else:
        return (diff(i + 1, k - 1, x, y) - diff(i, k - 1, x, y)) / (x[i + k] - x[i])

#divided differences
n = len(x)
dy = []
for k in range(n):
    dy.append(diff(0, k, x, y))
print("Divided Differences: \n", dy)

#Newton basis polynomials
def n(_x, k, x):
    v = 1
    for k in range(k):
        v *= (_x - x[k])
    return v

#Newton polynomials
def N(_x, x, dy):
    v = 0
    for k in range(len(x)):
        v += dy[k] * n(_x, k, x)
    return v

#Value of the Newton polynomial in the data points
for i in range(len(x)):
    print("N(%f) = %f" %(x[i], N(x[i], x, dy)))

#visualization of data points
plt.xlabel("x")
plt.ylabel("y")
plt.scatter(x, y)

#visualization of the Newton polynomial
h = 0.1
xi = 0
nx = []
ny = []
for j in range(50):
    nx.append(xi)
    ny.append(N(xi, x, dy))
    xi += h
plt.plot(nx, ny)

plt.show()