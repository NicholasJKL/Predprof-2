import sqlite3

conn = sqlite3.connect(r'info.db')
cur = conn.cursor()





cur.execute("SELECT * FROM groups;")
all_results = cur.fetchall()
cur.execute("SELECT * FROM app;")
all_results2 = cur.fetchall()
cur.execute("SELECT * FROM material;")
all_results3 = cur.fetchall()
cur.execute("SELECT * FROM digital;")
all_results4 = cur.fetchall()
cur.execute("SELECT * FROM analog;")
all_results5 = cur.fetchall()
cur.execute("SELECT * FROM hybrid;")
all_results6 = cur.fetchall()





