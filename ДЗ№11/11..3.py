import random  # PEP8 ругается на множественный импорт в одной строчке
import timeit
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict


def sort_test(your_list):
    """
    function checks if a given list is sorted
    """
    if all(your_list[i] <= your_list[i + 1] for i in range(len(your_list) - 1)):
        return True
    return False


def monkey_sort(s_list):
    """
    randomly shuffles your data until it will be sorted
    :return:sorted list
    """
    while not sort_test(s_list):
        random.shuffle(s_list)
    return s_list


def generator(n):
    numb_np = np.random.uniform(0, 100, n)
    return numb_np


end_data = defaultdict(list)
for u in range(7):  # size of your data
    data = []
    for p in range(10):  # number of repeats for statistics
        nmb = generator(u)
        data.append(timeit.timeit("monkey_sort(nmb)", "from __main__ import monkey_sort, sort_test, nmb"))
    end_data[u].extend(data)

plot = plt.boxplot(list(end_data.values()))
plt.title('Monkey sorting')
plt.xlabel('size of a massive')
plt.ylabel('time')
print(plot)


