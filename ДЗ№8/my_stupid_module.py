print('You managed to do this!')

def tree():
    t = '*'
    for i in range(7):
        print(t.center(30,' '), end='\n')
        t += 'O**'

def chitalka(b,i):
    y = 0
    while i <= 10:
        print(b+1, end='')
        y += 1
        i += 1
    return b+1, y

