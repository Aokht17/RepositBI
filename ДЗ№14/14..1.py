import pandas as pd

rd = pd.read_csv('C:/Users/User/PycharmProjects/RepositBI/5_modul/train.csv', usecols=[6,7,8,9])
rd.plot.hist()

