#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup
from datetime import datetime  

import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
addrs = ["https://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=1h", "https://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=1h&page=2"]

now_time = datetime.now()
print('실시간 네이버뮤직 차트')
print('현재시각 : %s.%s.%s %s:%s' % (str(now_time.year), str(now_time.month).zfill(2), str(now_time.day).zfill(2), str(now_time.hour).zfill(2), str(now_time.minute).zfill(2) ))

naver = requests.get(addrs[0], headers = header)
soup = BeautifulSoup(naver.text, 'html.parser')

titles = soup.select('tr._tracklist_move > td.name > a._title > span')
artist = soup.select('tr._tracklist_move > td._artist.artist > a._artist > span.ellipsis')

"""
현재 듀엣곡일 경우나 아티스트가 콜라보했을 경우에는 a태그내에서 확인하기 때문에 
순위와 곡이름, 아티스트명을 정해서 클래스화 시킬필요가 있을 것 같음
"""
for i in range(len(titles)):
	print('%3d위: %s - %s' % (i+1, titles[i].text, artist[i].text.strip()))