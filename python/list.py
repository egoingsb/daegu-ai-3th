import sqlite3
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
cur.execute('SELECT * FROM topics')
topics = cur.fetchall()
for id, title, body in topics:
  print(id, title, body)
cur.close()