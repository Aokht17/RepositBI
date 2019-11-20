print('You managed to do this!')

def tree():
    """
    draw a stupid christmas tree with * and O
    """
    t = '*'
    for i in range(7):
        print(t.center(30,' '), end='\n')
        t += 'O**'

def chitalka(b,i):
    """
    meaningless function
    :param b: int
    :param i: int
    :return: a number and how many times it was printed
    """
    y = 0
    while i <= 10:
        print(b+1, end='')
        y += 1
        i += 1
    return b+1, y
