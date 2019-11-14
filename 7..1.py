print('Over {0} people in the USA develop severe {2} each year, and {1}% of these people die' .format(1*10**6, round((10**7)*2.57/(10**6), 1),'sepsis'))
# x:.1 does not work in my version, as well as f-prefix

n = input('vvedite stroky').strip()
strok = '%s can be encoded as %s and consists of %s symbols' % (n, n.encode('UTF-8'), len(n))
print(strok.center(70, '*'))

chislo = 8
place = 'bathroom'
print(f'{chislo} little T-REXes are waiting for you in the {place} right now')