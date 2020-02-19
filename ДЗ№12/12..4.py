from itertools import product


def nucleotide_comb(n):
    """
    generator for all possible nucleotide sequences with length from 1 to n
    :return: list
    """
    nucl = 'ATCG'
    output = []
    for i in range(1, n+1):
        output.extend(map("".join, product(nucl, repeat=i)))
    yield output


for o in nucleotide_comb(2):
    print(*o)

