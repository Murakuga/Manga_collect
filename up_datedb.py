import sqlite3
from manga_cheak import cheak


def date_up():
    conn = sqlite3.connect("manga_cheak.sqlite3")
    c = conn.cursor()
    sql = "SELECT date, title, url FROM manga;"
    c.execute(sql)
    manga_info = c.fetchall()
    i = 0
    new_info = cheak()
    for j in manga_info:
        if j[0] != new_info[i]:
            c.execute('update manga set date = ? where title = ?', (
                    new_info[i], j[1]))
        i += 1
    conn.commit()
    c.close()
