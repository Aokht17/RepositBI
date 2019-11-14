def linear_search(spisok, x):
    """Returns the smallest index at which an item is found"""
    i = 0
    while i <= len(spisok)-1:
        if spisok[i] == x:
            return i
            break
        else:
            i += 1
    return None
