line = ('a cat ate a rat')  # есть строка
print(type(line))
line1 = line.split()  # перевод в лист№1
print(type(line1))
line2 = list(line)  # перевод в лист №2
line3 = tuple(line)  # в кортеж
print(type(line3))
line4 = set(line)  # в сэт
print(type(line4))
# ЭТО ОЧЕНЬ СКУЧНО
# из кортежа
line5 = str(line3)  
line6 = list(line3)
line7 = set(line3)
# из листа
line8 = tuple(line2)
line9 = set(line2)
line10 = str(line2)
# из сэта
line11 = str(line4)
line12 = tuple(line4)
line13 = list(line4)
