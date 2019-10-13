i = input('введите строку')
if i[0] == i[0].upper():
    print('Начинается с заглавной буквы')
else:
    print('Начинается с маленькой буквы')
print('всего', len(i), 'символов в строке')
print('в конце !!') if i[-1] and i[-2] == '!' else print('неожиданный финал')
print('fire встречается', i.count('fire'), 'раз(а)')
print(i.lower(), i.upper(), i.title())
