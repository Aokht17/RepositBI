import re

with open('2430AD.txt', 'r') as file:
    pat = re.compile(r'(?<![A-Za-z0-9.])\d+\.*\d+(?!\w)')
    num=[]
    for line in file:
        num += pat.findall(line)
    print(*num)
