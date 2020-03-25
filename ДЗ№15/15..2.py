import re

with open('2430AD.txt', 'r') as file:
    pat = re.compile(r'(\d+)')
    num=[]
    for line in file:
        num += pat.findall(line)
    print(*num)
