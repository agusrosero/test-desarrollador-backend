import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL,
              email TEXT NOT NULL)''')

c.execute("INSERT INTO users (username, email) VALUES ('user1', 'test1@example.com')")
c.execute("INSERT INTO users (username, email) VALUES ('user2', 'test2@example.com')")

conn.commit()
conn.close()
