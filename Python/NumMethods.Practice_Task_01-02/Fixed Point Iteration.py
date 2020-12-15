import math

print("Numerical Methods: Practice Task #02 / Example A ")

# x = log(1 + x)
# Fixed Point Iteration Method

n = 30
x1 = 0.5
x2 = 0
delta = 0

for x in range(n + 1):
    x2 = math.log(x1 + 1)
    delta = math.fabs(x2 - x1)
    print("#iter.", x, " x[n] = ", x1, "  x[n+1] = ", x2, " delta = ", delta, "\n ")
    x1 = x2
