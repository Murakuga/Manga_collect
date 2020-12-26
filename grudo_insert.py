from bs4 import BeautifulSoup
from urllib import request
import sqlite3

garudo_list = [
        "13933686331682726050", "13933686331686107473",
        "13933686331686107477", "13933686331682726073",
        "13933686331682726054", "13933686331682726059",
        "13933686331676444158"]

dbname = "manga_cheak.sqlite3"
conn = sqlite3.connect(dbname)
cur = conn.cursor()


def garudo_cheak():
    for i in range(len(garudo_list)):
        url = (
                    "https://comic-gardo.com/episode/"
                    + garudo_list[i]
                    )
        response = request.urlopen(url)
        soup = BeautifulSoup(response, 'html.parser')
        response.close()
        elems = soup.find("p", attrs={"class", "episode-header-date"})
        elems = elems.get_text()
        date = elems.replace(" ", "")
        date = date.replace("\n", "")
        title = soup.find("h1", attrs={"class", "series-header-title"})
        title = title.get_text()
        manga_data = [date, title, url]
        cur.execute('insert into manga values (?,?,?)', manga_data)
    cur.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    garudo_cheak()
