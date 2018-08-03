#-*- coding: utf-8 -*-
class music:
	def __init__(self, name, artist, rank, site):
		self.name = name
		self.artist = artist
		self.rank = rank
		self.site = site

	def music_print(self):
		string = self.name
		string += "|" + self.artist + "|" + self.rank + "|" + self.site
		print("%s" %( string ) )
"""		print("song : %s" % (self.name))
		print("artist : %s" % (self.artist))
		print("rank : %s" % (self.rank))
		print("site : %s" % (self.site))
"""

