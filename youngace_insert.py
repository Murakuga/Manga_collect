from bs4 import BeautifulSoup
from urllib import request

import re
import sqlite3

numbers = [
    "1000124", "1000013", "1000010", "1000117", "1000014", "1000121", "1000132"
    ]

dbname = "manga_cheak.sqlite3"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

for i in range(len(numbers)):
    url = "https://web-ace.jp/youngaceup/contents/"+numbers[i]+"/"
    response = request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    response.close()
    elems = soup.select("span.updated-date")
    text = str(elems[0])
    reg_obj = re.compile(r"<[^>]*?>")
    tag_str = text
    result = reg_obj.sub("", tag_str)
    titles = soup.find("div", attrs={"class", "credit"})
    title = titles.find('h1')
    t = str(title)
    t_obj = re.compile(r"<[^>]*?>")
    tag_title = t
    title_result = t_obj.sub("", tag_title)
    manga_data = [(result, title_result, url)]
    cur.executemany('insert into manga values (?,?,?)', manga_data)
conn.commit()
conn.close()
