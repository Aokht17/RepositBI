def reversi(p):
    """
returns reversed list
    :param p: list
    """
    p1 = p[::-1]
    return p1


def reversi2(o):
    """
    is analog of reversi function using recursion
    :param o: list
    """
    if not o:
        return []
    return [o.pop()] + reversi2(o)


