import sqlite3
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
id = input('id? ')
cur.execute('DELETE FROM topics WHERE id = ?', (id))
conn.commit()
conn.close()
