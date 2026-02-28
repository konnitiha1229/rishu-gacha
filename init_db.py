import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('CREATE TABLE classes (name TEXT, day TEXT, period INTEGER, faculty TEXT, difficulty INTEGER, syllabus_url TEXT)')
sample_classes = [('心理学入門', '月', 1, '文学部', 2, 'https://example.com/psyc')]
c.executemany('INSERT INTO classes VALUES (?,?,?,?,?,?)', sample_classes)
conn.commit()
conn.close()
print("DB作成完了")
