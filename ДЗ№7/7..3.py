import numpy as np
from itertools import count as count_from


ten_squares = [x**2 for x in range(11)]
print(ten_squares)

summa = [x + y for x in range(0, 4) for y in range(5, 9)]
print(summa)

non_gene_code = [x + '->' + y for x in 'ATCG' for y in 'ATCG' if x != y]
print(*non_gene_code)

a = [[j for j in range(i-2, i+1)] for i in range(3, 10, 3)]   # 3*3 выйдет от 0 до 8, или от 1 до 9
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

# или с помощью пакетов
count = count_from(0)
matrix = [[next(count) for _ in range(3)] for _ in range(3)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

# вообще можно через NumPy
Ztable = np.arange(9).reshape(3,3)
print(Ztable)