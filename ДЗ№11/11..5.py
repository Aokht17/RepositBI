import matplotlib.pyplot as plt
from random import random, randint
from scipy import sqrt, zeros


corners = [(0, 0), (0.5, sqrt(3) / 2), (1, 0)]  # corners of a regular triangle


def middle(p, q):
    return 0.5 * (p[0] + q[0]), 0.5 * (p[1] + q[1])


n = 1000  # number of steps
x = zeros(n)
y = zeros(n)

x[0] = random()
y[0] = random()
for i in range(1, n):
    k = randint(0, 2)  # random triangle vertex (0, 1 or 2 from the list)
    x[i], y[i] = middle(corners[k], (x[i - 1], y[i - 1]))

plt.scatter(x, y)
plt.show()