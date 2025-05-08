from __future__ import division, print_function, unicode_literals
import math
import numpy as np
import matplotlib.pyplot as plt

class Gradient:
    def grad(x):
        return 2*x+ 5*np.cos(x)

    def cost(x):
        return x**2 + 5*np.sin(x)

    def myGD1(alpha, x0, gra = 1e-3, loop = 1000):
        x = [x0]
        for it in range(loop):
            x_new = x[-1] - alpha*Gradient.grad(x[-1])
            if abs(Gradient.grad(x_new)) < gra:
                break
            x.append(x_new)
        return (x, it)





