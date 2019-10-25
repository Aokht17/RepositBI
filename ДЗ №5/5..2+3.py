from operator import itemgetter

war_and_peace = {}
war_and_peace['bolkonsky'] = "natasha"
war_and_peace['bolkonsky'] = 'oak'  # замена значения
war_and_peace.update({'natasha': 'pjer', 'nikola': 'maria', 'napoleon': 'cold_winter'})
print(war_and_peace)
del war_and_peace['nikola']
print(war_and_peace)
war_and_peace = {v: k for k,v in war_and_peace.items()}  # инвертирование считается за обращение к нескольким элементам?
print(war_and_peace)


print(war_and_peace.items())  # или почти то же самое

for key, value in war_and_peace.items():
    print(key, value)

for key in war_and_peace.keys():
    print(key, war_and_peace.get(key))


def my_function(d, val):  # самый неудобный способ
    for k, v in d.items():
        if v == val:
           return k


for value in war_and_peace.values():
    print(my_function(war_and_peace, value), value)

myview = itemgetter(war_and_peace)  # еще один странный оператор
print(myview)
