import sqlite3

connection = sqlite3.connect('books.db')

connection.execute('DROP TABLE IF EXISTS authors')
connection.execute('DROP TABLE IF EXISTS works')

connection.execute('''CREATE TABLE IF NOT EXISTS authors (author_id INTEGER PRIMARY KEY,
                                                            name TEXT,
                                                            surname TEXT,
                                                            birth INTEGER,
                                                            death INTEGER,
                                                            country TEXT,
                                                            UNIQUE (name, surname, country))''')
connection.execute('''CREATE TABLE IF NOT EXISTS works (work_id INTEGER PRIMARY KEY,
                                                            work_name TEXT,
                                                            year INTEGER,
                                                            type TEXT,
                                                            work_author INTEGER REFERENCES authors (author_id) ON UPDATE CASCADE,
                                                            UNIQUE (work_name,work_author)) ''')

query1 = '''INSERT INTO authors (name, surname, birth, death, country) VALUES (?,?,?,?,?)'''
list_aut = [('Aldous', 'Huxley', 1894, 1963, 'GB'), ('Hermann', 'Hesse', 1877, 1962, 'Germany'),
            ('Heinrich', 'Böll', 1917, 1985, 'Germany'), ('Boris', 'Vian', 1920, 1959, 'France'),
            ('Jean-Paul', 'Sartre', 1905, 1980, 'France')]
connection.executemany(query1, list_aut)

query2 = '''INSERT INTO works (work_name, year, type, work_author) VALUES (?,?,?,?)'''
list_work = [('The Glass Bead Game', 1943, 'novel', 2), ('Point Counter Point', 1928, 'novel', 1), ('Steppenwolf', 1927, 'novel', 2),
             ('Brave New World', 1932, 'novel', 1), ('Siddhartha', 1922, 'novel', 2), ('Mortal Coils', 1921, 'short stories', 1)]
connection.executemany(query2, list_work)

query3 = '''INSERT INTO works (work_name, year, type, work_author) VALUES (?,?,?,?)'''
list_work1 = [('The Clown', 1963, 'novel', 3), ('Foam of the Days', 1947, 'novel', 4), ('The Red Grass', 1950, 'novel', 4),
             ('Nausea', 1938, 'novel', 5), ('Group Portrait with Lady', 1971, 'novel', 3), ('No Exit', 1944, 'play', 5)]
connection.executemany(query3, list_work1)

connection.commit()
# Эта штука работает в SQL браузере и делает pivot таблицу. Я хотела запихнуть ее в саму таблицу и сделать обновляемой
# но я не знаю как(((
connection.execute(''' SELECT work_author as writer, COUNT(work_id) AS things   
                                                FROM works 
                                                GROUP BY work_author''')

connection.commit()
connection.close()