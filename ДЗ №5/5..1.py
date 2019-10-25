s = set()
s.add('abc')
s.add(3.7)
s.add((1,2,3))
print(s)
mixed_set = {2.0, "crocodile", (1, 2, 3)}
print(mixed_set)
print(s.intersection(mixed_set))  # если добавить update, изменится само начальное множество
print(s.difference(mixed_set))
print(s.symmetric_difference(mixed_set))
s.update(mixed_set)  # эта команда портит вывод (изменяет начальный сэт), поэтому я поставила ее в конец
print(s)
print(s.issubset(mixed_set))
print(s.issuperset(mixed_set))
