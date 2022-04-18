import sqlite3
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
id = input('id? ')
cur.execute('DELETE FROM topics WHERE id = ?', (id,))
conn.commit()
cur.execute('SELECT * FROM topics')
topics = cur.fetchall()
for topic in topics:
  print('id:', topic[0], 'title:', topic[1])