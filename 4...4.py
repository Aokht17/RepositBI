i = input('введите строку')
if i[0].isupper():
    print('Начинается с заглавной буквы')
else:
    print('Начинается с маленькой буквы')
print('всего', len(i), 'символов в строке')
print('в конце !!') if i.endswith('!!') else print('неожиданный финал')
print('fire встречается', i.count('fire'), 'раз(а)')
print(i.lower(), i.upper(), i.title())