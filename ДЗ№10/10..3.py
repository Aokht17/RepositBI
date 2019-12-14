import seaborn as sns
np_matrix = list([i*0.5 for i in range(-100, 100, 2)])
plot = sns.boxplot(data=np_matrix, color='yellow')
plot.set(xlabel='x', ylabel='y', title='ящик с усами')
print(plot)