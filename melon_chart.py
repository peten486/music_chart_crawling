#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup
from datetime import datetime  

import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
addr = 'https://www.melon.com/chart/index.htm'

now_time = datetime.now()
print('실시간 멜론 차트')
print('현재시각 : %s.%s.%s %s:%s' % (str(now_time.year), str(now_time.month).zfill(2), str(now_time.day).zfill(2), str(now_time.hour).zfill(2), str(now_time.minute).zfill(2) ))

melon = requests.get(addr, headers = header)
soup = BeautifulSoup(melon.text, 'html.parser')

chart_time_yyyymmdd = soup.select('div.multi_row > div > span.yyyymmdd > span')
chart_time_hhmm = soup.select('div.multi_row > div > span.hhmm > span')

print('차트시각 : %s %s' % ( chart_time_yyyymmdd[0].text, chart_time_hhmm[0].text ))

titles = soup.select('#lst50 > td > div > div > div.ellipsis.rank01 > span > a')
artist = soup.select('#lst50 > td > div > div > div.ellipsis.rank02 > span')

for i in range(len(titles)):
	print('%3d위: %s - %s' % (i+1, titles[i].text, artist[i].text))

titles = soup.select('#lst100 > td > div > div > div.ellipsis.rank01 > span > a')
artist = soup.select('#lst100 > td > div > div > div.ellipsis.rank02 > span')

for i in range(len(titles)):
	print('%3d위: %s - %s' % (i+51, titles[i].text, artist[i].text))