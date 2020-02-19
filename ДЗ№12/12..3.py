from itertools import product


ranks = [*range(2,11), 'J', 'Q', 'K', 'A']
ace = ['H', 'C', 'S', 'D']
standart_deck = list(product(ranks, ace))
for i in standart_deck:
    print(i)
print(len(list(product(ranks, ace))))
