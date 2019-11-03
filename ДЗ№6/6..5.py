def srednee(m):
    """
returns the mean of the list
    :param m: list of numbers(int, float)
    :return: mean (float)
    """
    summa = 0
    lenth = 0
    for elem in m:
        summa += elem
        lenth += 1
    return summa/lenth

