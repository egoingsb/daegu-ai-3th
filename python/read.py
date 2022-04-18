import sqlite3
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
id = input('id ? ')
cursor.execute('SELECT * FROM topics WHERE id = ?', (id,))
topics = cursor.fetchone()
print(topics);