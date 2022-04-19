from flask import Flask, request, redirect
import random
import sqlite3

app = Flask(__name__)

def template(content):
  conn = sqlite3.connect('db.sqlite3')
  cur = conn.cursor()
  cur.execute('SELECT * FROM topics')
  topics = cur.fetchall()
  print(topics)
  liTag = ''
  for topic in topics:
    liTag = liTag + f'<li><a href="/read/{topic[0]}">{topic[1]}</a></li>'
  return f'''
  <html>
    <body>
      <h1><a href="/">WEB</a></h1>
      <ol>
        {liTag}
      </ol>
      {content}
      
      <p><a href="/create">create</a></p>
    </body>
  </html>
  '''  

@app.route("/")
def index():
  return template('<h2>Welcome</h2>Hello, WEB')

@app.route("/read/<id>")
def read(id):
  conn = sqlite3.connect('db.sqlite3')
  cur = conn.cursor()
  cur.execute('SELECT * FROM topics WHERE id=?', (id,))
  topic = cur.fetchone()  
  return template(f'<h2>{topic[1]}</h2>{topic[2]}')
@app.route("/create")
def create():
  return template('''
  <h2>Create</h2>
  <form action="create_process" method="POST">
    <p><input type="text" name="title" placeholder="제목을 입력하세요"></p>
    <p><textarea name="body" placeholder="본문을 입력하세요"></textarea></p>
    <p><input type="submit"></p>
  </form>
  ''')
@app.route('/create_process', methods=['POST'])
def create_process():
  t = request.form['title']
  b = request.form['body']
  conn = sqlite3.connect('db.sqlite3')
  cur = conn.cursor()
  cur.execute('INSERT INTO topics (title, body) VALUES(?, ?)', (t,b))
  conn.commit()
  url = 'read/'+str(cur.lastrowid)
  return redirect(url)
app.run()