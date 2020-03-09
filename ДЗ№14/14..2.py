import pandas as pd


rf = pd.read_csv('C:/Users/User/PycharmProjects/RepositBI/5_modul/train.csv')
srednee = rf['matches'].mean()
header = ['pos','reads_all','mismatches', 'deletions', 'insertions']
rf.query('matches > @srednee').to_csv(r'train_part.csv',columns=header)


