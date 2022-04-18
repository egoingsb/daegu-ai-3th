import sqlite3
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
title = input('title? ')
body = input('body? ')
cur.execute('INSERT INTO topics (title, body) VALUES(?,?)', (title, body))
id = cur.lastrowid
conn.commit()
cur.execute('SELECT * FROM topics WHERE id = ?', (id,))
topic = cur.fetchone()
print(topic)
conn.close()