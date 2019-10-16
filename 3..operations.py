print('Закон Ома')
I = float(input('Сила тока='))
R = float(input('Сопротивление='))
U = I*R
print('Напряжение равно', U)  # например, при I=5.6 и R=9, напряжение будет равно 50.4

print('С из эн по ка')


def c_is_n_po_k(k, N):
    import math
    return int(math.factorial(N)/(math.factorial(k)*math.factorial(N-k)))


N = float(input('N='))
k = float(input('k='))
print(c_is_n_po_k(k, N))

print('Закон Мура')
m = int(input('сколько месяцев прошло?'))
print('количество транзисторов на кристалле интегральной схемы выросло примерно в {} раз(a)'.format(2**(m/24)))