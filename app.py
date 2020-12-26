import sqlite3
from flask import Flask, render_template
from manga_cheak import cheak
from up_datedb import date_up

app = Flask(__name__)


@app.route("/")
def index():
    conn = sqlite3.connect("manga_cheak.sqlite3")
    c = conn.cursor()
    sql = "SELECT date, title, url FROM manga;"
    c.execute(sql)
    manga_info = c.fetchall()
    i = 0
    new_info = cheak()
    manga = manga_info
    new_manga_info = []
    for j in manga_info:
        if j[0] != new_info[i]:
            new_manga_info.append((new_info[i], j[1], j[2]))
            del manga[i]
        i += 1
    return render_template(
        "index.html", manga_info=manga, new_manga_info=new_manga_info
                            )


date_up()

if __name__ == '__main__':
    app.run(debug=True)
