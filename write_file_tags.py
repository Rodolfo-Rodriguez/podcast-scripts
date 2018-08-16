#!/usr/bin/python2.7

# This Python file uses the following encoding: utf-8

import os
import sys
import mutagen
from mutagen.mp4 import MP4, MP4Cover
from mpd import MPDClient
from globals import global_values

if len(sys.argv) < 5:
  print '[ERROR] Uso: python ' + sys.argv[0] + ' <filename> <artist_tag> <album-tag> <title-tag>'
  sys.exit(2)

filename = sys.argv[1]
artist_tag = sys.argv[2]
album_tag = sys.argv[3]
title_tag = sys.argv[4]

song_ext = filename.split('.')[-1]

if song_ext == 'm4a':
  
  audio = MP4(filename)

  audio['\xa9ART'] = unicode(artist_tag,'utf-8')
  audio['\xa9nam'] = unicode(title_tag,'utf-8')
  audio['\xa9alb'] = unicode(album_tag,'utf-8')

  audio.save()

  print filename + ' --> MP4 | Artist: ' + artist_tag + ' | Album: ' + album_tag + ' | Title: ' + title_tag
