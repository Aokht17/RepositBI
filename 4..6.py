a = int(input('введите а'))
b = int(input('введите в'))
c = int(input('введите с'))
if a + b < c or a + c < b or b + c < a:
    print('нет такого треугольника')
elif a == b == c:
    print('равносторонний')
elif a == b or b == c or a == c:
    print('равнобедренный')
else:
    print('разносторонний')

