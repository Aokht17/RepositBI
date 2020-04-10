import re
import seaborn as sns
import matplotlib.pyplot as plt


with open('2430AD.txt', 'r') as file:
    pat = re.compile(r'[A-Za-z]\.?\w*')  # ok, my parser cut 'didn't' as 'didn' and 't', it's not alright
    words = set()
    for line in file:
        for i in pat.findall(line):
            words.add(i.lower())

lens = [len(i) for i in words]
ax = sns.distplot(tuple(lens))
ax.set_title("Unique words' length distribution")
ax.set(xlabel='Word length', ylabel='Frequency')
plt.show()
