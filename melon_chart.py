#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup
import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
addr = 'https://www.melon.com/chart/index.htm'
melon = requests.get(addr, headers = header)
soup = BeautifulSoup(melon.text, 'html.parser')
titles = soup.select('#lst50 > td > div > div > div.ellipsis.rank01 > span > a')
artist = soup.select('#lst50 > td > div > div > div.ellipsis.rank02 > span')

print('실시간 멜론 차트\n')
for i in range(50):
        print( '%3d위: %s - %s'%(i+1, titles[i].text, artist[i].text))
