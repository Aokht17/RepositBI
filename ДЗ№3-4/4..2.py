tulpan = ()
tuple1 = (1, 7, 79, 'word', [2, 4])
tulpan += tuple1
print(tulpan)
# немного читерства
tulpan = list(tulpan)
tulpan.append(79)
tulpan += '78'
del tulpan[-1]
tulpan[1] = 10
tulpan = tuple(tulpan)  # возвращаемся
print(tulpan)
print(tulpan.count(79))
print(len(tulpan))
