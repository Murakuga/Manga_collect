from clean_text import clean_ace_text, clean_garudo_text, clean_walker_text
from access_web import access_ace, access_walker, garudo_cheak

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
list_result = []


def cheak():
    for i in range(len(young_ace_numbers)):
        access_ace_text = access_ace(i)
        cat = clean_ace_text(access_ace_text)
        list_result.append(cat)
    for j in range(len(comic_walker_numbers)):
        access_walker_text = access_walker(j)
        cwt = clean_walker_text(access_walker_text)
        list_result.append(cwt)
    for k in range(len(garudo_list)):
        text = garudo_cheak(k)
        cgt = clean_garudo_text(text)
        list_result.append(cgt)
    return list_result
