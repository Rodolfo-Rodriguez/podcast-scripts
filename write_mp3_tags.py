#!/usr/bin/python2.7

# This Python file uses the following encoding: utf-8

import os
import sys
import mutagen
from mpd import MPDClient
import eyed3
from globals import global_values,ep_dirs,pod_dirs,artist_tags

if len(sys.argv) < 4:
  print '[ERROR] Uso: python ' + sys.argv[0] + ' <filename> <pod-nick> <title-tag>'
  sys.exit(2)

filename = sys.argv[1]
pod_nick = sys.argv[2]
title_tag = sys.argv[3]

if (pod_nick in pod_dirs):
	pod_dir = pod_dirs[pod_nick]
elif (pod_nick in ep_dirs):
	pod_dir = ep_dirs[pod_nick]
else:
	print '[ERROR] No existe el podcast [' + pod_nick + ']'
	sys.exit(2)

artist_tag = artist_tags[pod_nick]

pod_uri = global_values['base_pod_uri_path'] + '/' + pod_dir

mpd_client = global_values['mpd_client']
mpd_port = global_values['mpd_port']

audio = eyed3.load(filename)

audio.initTag()

audio.tag.title = title_tag.decode('utf-8')
audio.tag.artist = artist_tag.decode('utf-8')

audio.tag.save()

print filename + ' --> Title: ' + title_tag + 'Artist: ' + artist_tag

client = MPDClient()
client.connect(mpd_client, mpd_port)
client.update(pod_uri)
client.close()
