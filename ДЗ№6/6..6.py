def moda(rt):
    """
    returns the most frequent item(s)
    :param rt: list
    :return: set of most frequent item(s)
    """
    vstr = 1
    znachenia = set()
    for elem in rt:
        if vstr < rt.count(elem):
            vstr = rt.count(elem)
            znachenia.clear()
            znachenia.add(elem)
        elif vstr == rt.count(elem):
            znachenia.add(elem)
    return znachenia





