def poluchatel(lst, n):
    """
  takes the specified item from the collection
    :param lst: dict, list, etc
    :param n: number or key of element
    """
    if type(lst) is dict:
        i = lst.get(n)
    else:
        i = lst[n]
    return i

