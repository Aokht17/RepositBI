from itertools import product


def nucleotide_comb(n):
    """
    generator for all possible nucleotide sequences with length from 1 to n
    :return: list
    """
    nucl = 'ATCG'
    for i in range(1, n+1):
        for j in map("".join, product(nucl, repeat=i)):
            yield j


for o in nucleotide_comb(2):
    print(*o)
