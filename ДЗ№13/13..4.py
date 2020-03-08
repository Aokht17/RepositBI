import seaborn as sns
import matplotlib.pyplot as plt
from itertools import product
import re


class UsefulStatistics():

    def __init__(self, fasta_path):
        self.fasta_path = fasta_path

    def __str__(self):
        return self.fasta_path

    def how_many_seq(self):
        """
    returns the number of sequences in fasta
        """
        count = 0
        with open(self.fasta_path) as file:
            for lines in file:
                count += 1
        return int(count/2)

    def histogram(self):
        """
    creates a histogram and fit a kernel density estimate for distribution of lines' length in fasta file
        :return: none
        """
        with open(self.fasta_path) as file:
            app = []
            for line in file:
                if not line.startswith('>'):
                    app.append(len(line))
        sns.distplot(tuple(app))

    def GC_percent(self):
        """
        returns the percent of G and C in sequences
        """
        percent = 0
        total = 0
        with open(self.fasta_path) as file:
            for lines in file:
                percent += lines.count('C')+lines.count('G')
                total += len(lines)
        return round(percent*100/total, 3)

    def hist_4mers(self):
        """
        creates a bar of 4-mers frequences
        :return: none
        """
        output = map("".join, product('ATCG', repeat=4))
        dict_4mers = {i: 0 for i in output}
        with open(self.fasta_path) as file:
            for lines in file:
                if not lines.startswith('>'):
                    for key in dict_4mers:
                        dict_4mers[key] += sum(1 for i in range(len(lines)) if lines.startswith(key, i))
        empty_keys = [k for k, v in dict_4mers.items() if not v]
        for k in empty_keys:
            del dict_4mers[k]

        labels, values = zip(*dict_4mers.items())
        plt.bar(labels, values, color='r')
        plt.title('Frequences of 4-mers')
        plt.show()

    def n_conter(self):
        """
        creates a line plot of N frequency in each position of your sequences
        :return: none
        """
        with open(self.fasta_path) as file:
            app = []
            for line in file:
                if not line.startswith('>'):
                    app.append(len(line))
            ma_x = max(app)
            dict_dist = {i: 0 for i in range(ma_x)}
        with open(self.fasta_path) as file:
            for lines in file:
                for m in re.finditer('N', lines):
                    # можно также через n for n in range(len(lines)) if lines.find('N', n) == n]
                    dict_dist[m.start()] += 1
        labels, values = zip(*dict_dist.items())
        plt.plot(labels, values, color='r')
        plt.title('N frequences')
        plt.show()

    def implement(self):
        """
        implementation of all class methods on your fasta
        """
        with open(self.fasta_path) as file:
            print(self.__str__())
            print('total number of sequences:', self.how_many_seq())
            print('percent of GC:', self.GC_percent(), '%')
            self.histogram()
            self.hist_4mers()
            self.n_conter()




a = UsefulStatistics('my_fasta')
a.implement()















