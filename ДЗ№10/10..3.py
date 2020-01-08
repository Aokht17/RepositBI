import seaborn as sns


np_matrix = list([i for i in range(-50, 50, 2)])
plot = sns.boxplot(data=np_matrix, color='yellow')
plot.set(xlabel='x', ylabel='y', title='ящик с усами')
print(plot)
