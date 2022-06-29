import requests
import os
from bs4 import BeautifulSoup as bs


def getHtml(url):
    try:
        res = requests.get(url)
        return res.text
    except:
        return False


def getData(html):
    soup = bs(html, 'html.parser')
    pics = soup.select('.photos a')
    print(len(pics))
    cmd_list = []
    for pic in pics:
        print(pic)
        cmds = 'you-get' + " " + pic['data-lazy']
        cmd_list.append(cmds)

    for each in cmd_list:
        os.system(each)


if __name__ == "__main__":
    url = 'https://baoting.s.gifshow.com/user/769994571'
    getData(getHtml(url))