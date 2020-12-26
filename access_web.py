from bs4 import BeautifulSoup
from urllib import request


young_ace_numbers = [
    "1000124", "1000013", "1000010",
    "1000117", "1000014", "1000121", "1000132"]
comic_walker_numbers = [
    "KDCW_AM01200774010000_68",
    "KDCW_AM17201404010000_68"]
garudo_list = [
        "13933686331682726050", "13933686331686107473",
        "13933686331686107477", "13933686331682726073",
        "13933686331682726054", "13933686331682726059",
        "13933686331676444158"]


def access_ace(number_i):
    url = (
            "https://web-ace.jp/youngaceup/contents/"
            + young_ace_numbers[number_i] + "/"
            )
    response = request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    response.close()
    elems = soup.select("span.updated-date")
    text_i = elems[0]
    return text_i


def access_walker(number_j):
    url = (
        "https://comic-walker.com/contents/detail/"
        + comic_walker_numbers[number_j] + "/"
        )
    response = request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    response.close()
    elems = soup.find("span", attrs={"class", "comicIndex-date"})
    text_j = str(elems)
    return text_j


def garudo_cheak(garudo_number):
    url = (
                    "https://comic-gardo.com/episode/"
                    + garudo_list[garudo_number]
                    )
    response = request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    response.close()
    return soup
