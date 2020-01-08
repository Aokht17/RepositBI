import matplotlib.pyplot as plt
import numpy as np
import random
import timeit


def generator_1(n):  # generator №1  for numpy
    numb_np = np.random.uniform(0, 1, n)
    return numb_np


def generator_2(n):  # generator №2  for random
    numb_rand = []
    for x in range(n):
        numb_rand.append(random.randint(0, 1))
    return numb_rand


data_1 = []
data_2 = []
for i in range(10):  # I set 10 because my computer "thinks" for a very long time
    data_1.append(timeit.timeit("generator_1(i)", "from __main__ import generator_1, i"))
    data_2.append(timeit.timeit("generator_2(i)", "from __main__ import generator_2, i"))

x = range(10)
plt.title('Comparison')
plt.xlabel('how many numbers')
plt.ylabel('time')
plt.grid(True)
plt.plot(x, data_1)
plt.plot(x, data_2)
plt.legend(['numpy ', 'random'], loc='upper left')
plt.show()




