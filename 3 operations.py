print ('Закон Ома\n ','Сила тока=')
I=float(input())
print ('Сопротивление=')
R=float(input())
U=I*R
print ('Напряжение равно',U) # например, при I=5.6 и R=9, напряжение будет равно 50.4

print ('С из эн по ка')
def c_is_n_po_k(k,N):
    import math
    return int(math.factorial(N)/(math.factorial(k)*math.factorial(N-k)))
print ('N=')
N=float(input())
print ('k=')
k=float(input())
print (c_is_n_po_k (k,N))

print ('Закон Мура\n', 'сколько месяцев прошло?')
m=int(input())
print ('количество транзисторов на кристалле интегральной схемы выросло примерно в {} раз(a)'.format(2**(m/24)))