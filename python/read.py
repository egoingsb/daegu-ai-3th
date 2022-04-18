import sqlite3
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
id = input('id? ')
cur.execute('SELECT * FROM topics WHERE id = ?', [id])
topic = cur.fetchone()
print(topic)