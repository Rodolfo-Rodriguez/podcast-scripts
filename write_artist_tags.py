#!/usr/bin/python2.7

# This Python file uses the following encoding: utf-8

import os
import sys
import mutagen
from mutagen.mp4 import MP4, MP4Cover
from mpd import MPDClient
import eyed3
from globals import global_values

if len(sys.argv) < 3:
  print '[ERRORR] Uso: ' + sys.argv[0] + ' <album-rel-dir> <artist-tag>'
  print '         Eje: ' + sys.argv[0] + " \'Uruguay/Buitres/1991 - BDDL1-La Bruja\' \'Buitres\'"
  sys.exit(2)

album_dir = sys.argv[1]
artist_tag = sys.argv[2]

album_full_dir = global_values['base_music_path'] + '/' + album_dir

album_uri = global_values['base_music_uri_path'] + '/' + album_dir

mpd_client = global_values['mpd_client']
mpd_port = global_values['mpd_port']

for filename in os.listdir(album_full_dir):
	song_ext = filename.split('.')[-1]
	if song_ext == 'm4a':
  		audio = MP4(album_full_dir + '/' + filename)
		audio['\xa9art'] = unicode(artist_tag,'utf-8')
		audio.save()
		print filename + ' --> [MP4] Artist: ' + artist_tag

client = MPDClient()
client.connect(mpd_client, mpd_port)
client.update(album_uri)
client.close()
