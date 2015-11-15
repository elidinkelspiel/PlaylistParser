# coding=utf-8
__author__='edinkelspiel'


import iTunes_parser as ip
import time

print str(time.time())

docroot = ip.set_docroot(raw_input("enter file location: "))

songlist = ip.pass_songs_to_list(docroot)

a = open(str(time.time()) + ".txt", 'w')

for song in songlist:
    a.write(song.encoded_string() + "\n\n")