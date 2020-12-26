import re


def clean_ace_text(ace_text):
    result = ace_text.get_text()
    return result


def clean_walker_text(walker_text):
    reg_obj = re.compile(r"<[^>]*?>")
    result = reg_obj.sub("", walker_text)
    result = result.replace("更新", "")
    result = result.replace(" ", "日")
    result = result.replace("/", "年", 1)
    result = result.replace("/", "月", 1)
    return result


def clean_garudo_text(garudo_text):
    elems = garudo_text.find("p", attrs={"class", "episode-header-date"})
    elems = elems.get_text()
    date = elems.replace(" ", "")
    date = date.replace("\n", "")
    return date
