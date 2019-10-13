interesting_numbers = (3, 2, 5, 7, 14, 26, 32, 31, 37)
sum = 0
for i in interesting_numbers:
    if i % 2 == 0:
        sum += i
print(sum)

