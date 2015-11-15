# coding=utf-8
__author__='edinkelspiel'

import xml.etree.ElementTree as ElementTree

def set_docroot(file):
    return ElementTree.parse(file).getroot()

class Song:
    def __init__(self, name, album, artist, album_artist, year):
        self.name = name
        self.album = album
        self.artist = artist
        self.album_artist = album_artist
        self.year = year

    def to_string(self):
        return "%s | %s | %s | %s | %s" %(self.name, self.album, self.artist, self.album_artist, self.year)

    def encoded_string(self):
        return self.to_string().encode('utf-8')

def parse_info_to_song(import_dict):
    import_dict["Name"]
    return Song(import_dict["Name"], import_dict["Album"], import_dict["Artist"], import_dict["Album Artist"], import_dict["Year"])

def pass_songs_to_list(docroot):
    songlist = []
    for child in docroot:
        for dict in child:
            for a in dict:
                previous = None
                important_info = {
                    "Name" : "N/A",
                    "Album" : "N/A",
                    "Album Artist" : "N/A",
                    "Year" : "N/A",
                    "Artist" : "N/A"
                }
                for b in a:
                    if previous in ["Name", "Album", "Album Artist", "Year", "Artist"]:
                        important_info[previous] = b.text
                    previous = b.text
                to_pass = parse_info_to_song(important_info)
                if to_pass.to_string() != "N/A | N/A | N/A | N/A | N/A":
                    songlist.append(parse_info_to_song(important_info))
    return songlist

k = 0
for song in pass_songs_to_list(set_docroot("myXML.xml")):
    k += 1
    print k, song.to_string()