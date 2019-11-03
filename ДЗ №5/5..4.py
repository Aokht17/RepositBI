stroka = input('введите строку')
if stroka[0] == ' ':
    print('строка начинается с пробела')
elif stroka[0].isalpha():
    print('строка начинается с буквы', stroka[0])
elif stroka[0].isdigit():
    print('строка начинается с цифры', stroka[0])
else:
    print('строка начинается с другого символа:', stroka[0])
