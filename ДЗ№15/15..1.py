import re

with open('references.txt', 'r') as file, open('ftps', 'w') as urls:
    pat = re.compile(r'(?!\W)ftp\.[A-Za-z0-9./_#]+')
    for lines in file:
        for line in pat.findall(lines):
            urls.write(line)
            urls.write("\n")
    


