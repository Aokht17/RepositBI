spisok = []
spisok += '45'
spisok.append (65)
spisok += 'letters'
spisok.append('summer')
spisok.insert(1, [3,4,6])
appendix = ['will', 'last', 'forever']
print (spisok + appendix)
print (spisok)
spisok.extend(appendix)
print (spisok)
spisok.remove (65)
spisok.pop (5)
del spisok[0]
spisok[1] = 10
print (spisok.count ('e'))
print (len(spisok))