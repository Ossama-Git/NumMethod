import math


def bisection_method(x_1, x_2):
    i = 1
    c = 0
    while True:
        f_x = function(x_1)
        y = (x_1 + x_2) / 2
        f_y = function(y)

        sig = f_x * f_y

        print("iterator", i, "value", " ", y)
        if i > 1:
            error = math.fabs((y - c) / y)
            if error == 0:
                print(" ")
                print("the answer : ", y)
                break

        if sig > 0:
            x_1 = y
        elif sig < 0:
            x_2 = y
        c = y
        i = i + 1


def function(x):
    f = math.pow(x, 6) - x - 1
    return f


bisection_method(0, 2)
