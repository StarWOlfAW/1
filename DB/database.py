import sqlite3
import uuid
con = sqlite3.connect("lessondb.db")
cur = con.cursor()
##for x in range(1000000):
##    g = cur.execute("INSERT INTO users (email, password, city) VALUES  (?, '14789', ?)", [str(uuid.uuid4()),str(uuid.uuid4())])
r = cur.execute("SELECT id, email FROM users WHERE city ='8b5de243-60e5-4c2b-b92a-1f0aaafda36b'")
con.commit()
print(r.fetchall())
con.close()