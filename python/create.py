import sqlite3
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
title = input('title? ')
body = input('body? ')
cur.execute('INSERT INTO topics (title, body) VALUES(?, ?)', (title, body))
conn.commit()
conn.close()