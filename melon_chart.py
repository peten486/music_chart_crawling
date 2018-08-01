#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup
from datetime import datetime  

import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
addr = 'https://www.melon.com/chart/index.htm'
melon = requests.get(addr, headers = header)
soup = BeautifulSoup(melon.text, 'html.parser')
titles = soup.select('#lst50 > td > div > div > div.ellipsis.rank01 > span > a')
artist = soup.select('#lst50 > td > div > div > div.ellipsis.rank02 > span')

print('실시간 멜론 차트')
print('현재시각 :  %d-%d-%s' % (datetime.now().year, datetime.now().month, datetime.now().day))
for i in range(50):
        print( '%3d위: %s - %2d'%(i+1, titles[i].text, artist[i].text))
