import re

with open('2430AD.txt', 'r') as file:
    pat = re.compile(r'(\w*[aA]\w*)')
    num=[]
    for line in file:
        num += pat.findall(line)
    for i in num:
        print(i, end='\n')