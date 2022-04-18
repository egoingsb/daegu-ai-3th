import sqlite3
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
id = input('id?')
cur.execute('SELECT * FROM topics WHERE id=?', (id,))
topic=cur.fetchone()
title = input(f'title? ({topic[1]})')
body = input(f'body? ({topic[2]})')

cur.execute('UPDATE topics SET title=?, body=? WHERE id=?', (title, body, id))
conn.commit()

cur.execute('SELECT * FROM topics WHERE id=?', (id, ))
topic = cur.fetchone()
print('id:', topic[0], 'title:', topic[1], 'body:', topic[2])
conn.close()