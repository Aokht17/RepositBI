import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')

connection.execute('DROP TABLE IF EXISTS authors')
connection.execute('DROP TABLE IF EXISTS works')

connection.execute('''PRAGMA FOREIGN_KEYS=ON''')
connection.execute('''CREATE TABLE authors (author_id INTEGER PRIMARY KEY,
                                                            name TEXT,
                                                            surname TEXT,
                                                            birth INTEGER,
                                                            death INTEGER,
                                                            country TEXT,
                                                            UNIQUE (name, surname, country))''')
connection.execute('''CREATE TABLE works (work_id INTEGER PRIMARY KEY,
                                                            work_name TEXT,
                                                            year INTEGER,
                                                            type TEXT,
                                                            work_author INTEGER REFERENCES authors (author_id) ON UPDATE CASCADE,
                                                            UNIQUE (work_name,work_author)) ''')
df = pd.read_csv('authors.csv', sep=';')
df.to_sql('authors',connection, if_exists='append', index=False)

df_2 = pd.read_csv('works.csv', sep=';')
df_2.to_sql('works', connection, if_exists='append', index=False)

#connection.execute("""UPDATE authors SET author_id = 100 WHERE name = 'Aldous'""")
connection.commit()
connection.execute('''CREATE TABLE content (number INTEGER PRIMARY KEY,
                                                            writer_id INTEGER,
                                                            total_things INTEGER)''')

cur = connection.cursor()
cur.execute(''' SELECT work_author as writer_id, COUNT(work_id) AS total_things   
                                                FROM works 
                                              GROUP BY work_author''')

cur.executemany('''INSERT INTO content (writer_id, total_things) VALUES (?,?)''', cur.fetchall())

connection.commit()
connection.close()
