# -*- coding: utf-8 -*-

import requests
import re
import os

pic_search = u"https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={key_word}&pn={pn_no}&gsm=64 &ct=&ic=0&lm=-1&width=0&height=0"


def download_pic(word):
    pic_url_set = set()
    for i in range(10):
        html = requests.get(pic_search.format(key_word=word, pn_no=i)).text

        pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
        pic_url_set.update(pic_url)

    # mkdir folder of key word
    folder_path = '/Users/xingzhiyuan/Documents/pictures/%s/' % word
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # download p
    n = 0
    for pic in pic_url_set:
        print pic
        try:
            pic_obj = requests.get(pic, timeout=10)
            if not pic_obj.ok:
                print "can not download"
                continue

        except requests.RequestException:
            print "can not download"
            continue

        with open(folder_path + str(n) + '.jpg', 'wb') as fp:
            print folder_path + str(n) + '.jpg'
            fp.write(pic_obj.content)
        n += 1


if __name__ == "__main__":
    download_pic(u"QQ头像")
