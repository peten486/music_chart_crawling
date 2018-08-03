#-*- coding: utf-8 -*-
import sys
import requests
import song

reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup
from datetime import datetime  

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
addrs = ["https://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=1h", "https://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=1h&page=2"]

now_time = datetime.now()
print('실시간 네이버뮤직 차트')
print('현재시각 : %s.%s.%s %s:%s' % (str(now_time.year), str(now_time.month).zfill(2), str(now_time.day).zfill(2), str(now_time.hour).zfill(2), str(now_time.minute).zfill(2) ))

songs = []


for idx in range(len(addrs)):
	naver = requests.get(addrs[idx], headers = header)
	soup = BeautifulSoup(naver.text, 'html.parser')
	body = soup.select('tbody tr')[1:51]

	for i in range(len(body)):
		tmp_tag = body[i]

		rank = tmp_tag.select('td.ranking')[0].get_text()
		name = tmp_tag.select('td.name > a._title > span')[0].get_text()
	
		try:
			artist = tmp_tag.select('td._artist > a > span')[0].get_text()
			artist = artist[15:-4]
		except IndexError:
			artist = tmp_tag.select('td._artist.artist.no_ell2 > a')[0].get_text()

		temp = name + '|' + artist + '|' + rank + '|NM'
		songs.append(song.music(name, artist, rank, "NM"))

for i in range(len(songs)):
	print('%s위: %s - %s' % (songs[i].rank, songs[i].name, songs[i].artist ))


"""
	주지마 - 로꼬, 화사인데,,,, 
	현재는 로꼬만 입력이 된다... 
	어떻게 화사도 입력할 수 있을까 고민을 해봐야할 듯 함..
"""