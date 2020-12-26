import sqlite3

dbname = "manga_cheak.sqlite3"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute(
    "CREATE TABLE manga(date string, title string, url string)"
    )

conn.commit()
conn.close()
