def monk(file1, file2, o=0, n=None):
    """
    rewrite lines with numbers in order(o, n) from file1 to file2
    :param
    o: int
    :param
    n: int, n > o
    :return: none
    """

    if n is None:
        n = sum(1 for line in open(file1))

    with open(file1, 'r') as from_where, open(file2, 'w') as destination:
        for i, line in enumerate(from_where):
            if o <= i <= n:
                destination.write(line)



