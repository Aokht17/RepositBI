def maximum(s):
    """
    Function returns the largest number in a set
    :param s: list of iterable
    :return: the biggest item
    """
    m = s[0]
    for i in s:
        if i > m:
            m = i
    return m

