seq1 = [1, 'i', [1, 2, 3], True, False, 7, '', 'ooo']
seq2 = [5.0, 98.4, 0, 101.8, '123']
seq3 = (1, 3, 8, 456, 89.7, 9000)
result1 = list(map(lambda i: i is True, seq1))
result2 = list(map(int, seq2))
result3 = list(map(lambda x: (x*45-67)**0.5, seq3))
result4 = list(filter(None, seq1))
result5 = list(filter(lambda x: x > 6, seq3))
result6 = list(filter(lambda x: type(x) is str, seq2))

print(result1, result2, result3)
print(result4, result5, result6)
