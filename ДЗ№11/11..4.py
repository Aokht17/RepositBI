import random
import numpy
import matplotlib.pyplot as plt


def random_walk(number_of_steps):
    """
    2D visualization of random walk
    :param number_of_steps: int
    :return: scatter plot
    """

    x = numpy.zeros(number_of_steps)
    y = numpy.zeros(number_of_steps)
    for i in range(number_of_steps):
        step = random.randint(-1, 2)
        if step == 1:  # 1 for right
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif step == -1:  # -1 for left
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif step == 2:  # 2 (up)
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
        else:  # 0 (down)
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
    plt.title("Random Walk ($n = " + str(number_of_steps) + "$ steps)")
    plt.scatter(x, y, color='violet', s=0.5)
    plt.savefig('random walk')


random_walk(100000)