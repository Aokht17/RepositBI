import sqlite3


connection = sqlite3.connect('learners1.db')
connection.execute('''CREATE TABLE IF NOT EXISTS learners (learners_id INTEGER PRIMARY KEY,
                                                            first_name TEXT, 
                                                            last_name TEXT,
                                                            test_score INTEGER,
                                                            offsets INTEGER,
                                                            UNIQUE (first_name, last_name))''')

query1 = '''INSERT INTO learners (first_name, last_name, test_score, offsets) VALUES (?,?,?,?)'''
learners = [('Masha', 'Petrova', 8, 2),('Katya', 'Ivanova', 10, 3),('Vasya', 'Sydorov', 6, 0), ('Olya', 'Sydorova', 5, 2),
            ('Ilya', 'Sanechkin', 7, 2)]
connection.executemany(query1, learners)

connection.execute('''CREATE TABLE IF NOT EXISTS attendance (
attendance_id INTEGER PRIMARY KEY,
course_id INTEGER,
learner_id INTEGER CASCADE,
FOREIGN KEY (learner_id) REFERENCES learners (learner_id)
)''')

connection.execute(''' UPDATE learners
            SET offsets = offsets + 1  WHERE test_score > 5''')
connection.execute(''' DELETE FROM learners
            WHERE offsets < 2''')

connection.commit()
connection.close()