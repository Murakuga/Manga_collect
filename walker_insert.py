import sqlite3
from bs4 import BeautifulSoup
from urllib import request
import re

conn = sqlite3.connect('manga_cheak.sqlite3')
c = conn.cursor()

numbers = ["KDCW_AM01200774010000_68", "KDCW_AM17201404010000_68"]
manga_id = [1200, 1720, 1120]

for i in range(len(numbers)):
    url = "https://comic-walker.com/contents/detail/" + numbers[i] + "/"
    response = request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    response.close()
    elems = soup.find("span", attrs={"class", "comicIndex-date"})
    text = str(elems)
    reg_obj = re.compile(r"<[^>]*?>")
    tag_str = text
    result = reg_obj.sub("", tag_str)
    result = result.replace("更新", "")
    result = result.replace(" ", "日")
    result = result.replace("/", "年", 1)
    result = result.replace("/", "月", 1)
    titles = soup.find("div", attrs={"class", "comicIndex-box"})
    title = titles.find('h1')
    t = str(title)
    t_obj = re.compile(r"<[^>]*?>")
    tag_title = t
    title_result = t_obj.sub("", tag_title)
    manga_date = [result, title_result, url]
    c.execute('insert into manga values (?,?,?)', manga_date)

c.close()
conn.commit()
conn.close()
