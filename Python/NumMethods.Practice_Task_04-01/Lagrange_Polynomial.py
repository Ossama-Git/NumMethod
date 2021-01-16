from matplotlib import pyplot as plt

# data points
x = [1.0, 2.0, 2.5, 3.0, 5.0]
y = [1.2, 3.1, 4.0, 2.1, 1.0]


# Lagrange interpolation
def lagrange(_x, x, y):
    p = 0.0  # Lagrange polynomial value
    n = len(x)
    for k in range(n):
        L = 1.0
        for i in range(n):
            if i != k:
                L *= (_x - x[i]) / (x[k] - x[i])
        p += y[k] * L
    return p


print("Lagrange polynomial values in the data points:")
for xi in x:
    yi = lagrange(xi, x, y)
    print("p(%f) = %f" % (xi, yi))

N = 60
h = 0.1
xi = -1
lx = []
ly = []
for j in range(N):
    yi = lagrange(xi, x, y)
    lx.append(xi)
    ly.append(yi)
    xi += h

plt.xlabel("x")
plt.ylabel("y")

# visualization of data points
plt.scatter(x, y)
# visualize Lagrange polynomial
plt.plot(lx, ly)

plt.show()