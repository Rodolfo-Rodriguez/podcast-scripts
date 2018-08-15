#!/usr/bin/python2.7

import os, sys
import os.path
import xml.etree.ElementTree as ET
import wget
from mpd import MPDClient
from globals import global_values,ep_dirs,playlist_max_files

pod_nick_str = ' [ '
for pdir in ep_dirs:
	pod_nick_str = pod_nick_str + pdir + ' | '
pod_nick_str = pod_nick_str.rstrip(' |') + ' ]'

if len(sys.argv) < 2:
  print '[ERROR] Uso: python2.7 ' + sys.argv[0] + pod_nick_str 
  sys.exit(2)

pod_nick = sys.argv[1]

if not(pod_nick in ep_dirs):
  print '[ERROR] No existe el podcast [' + pod_nick + ']'
  sys.exit(2)

pod_dir = ep_dirs[pod_nick]
pod_full_dir = global_values['base_pod_path'] + '/' + pod_dir

feed_url = global_values['ep_base_url'] + '/' + pod_dir + '/' + pod_nick + '.m3u'
pod_ep_file = pod_full_dir + '/' + global_values['local_ep_file']
down_ep_file = pod_full_dir + '/' + global_values['down_ep_file']

pod_uri = global_values['base_pod_uri_path'] + '/' + pod_dir
playlist_file = global_values['playlist_base_path'] + '/' + pod_dir + '.m3u'

mpd_client = global_values['mpd_client']
mpd_port = global_values['mpd_port']

max_pl_files = playlist_max_files[pod_nick]


####################################################################################
# Download and parse feed file 
####################################################################################

if os.path.isfile(pod_ep_file):
	os.remove(pod_ep_file)

print '==> Donwloading Feed File: ' + feed_url
wget.download(feed_url, pod_ep_file)
print '\n'

down_episodes = [line.rstrip('\n') for line in open(down_ep_file)]
pod_episodes = [line.rstrip('\n') for line in open(pod_ep_file)]

####################################################################################
# Check Downloaded Episodes
####################################################################################

down_ep_f = open(down_ep_file,'a')

for ep in pod_episodes:
  if not(ep in down_episodes):
    ep_filename = pod_full_dir + '/' + (ep.split('/')[-1]).split('?')[0]
    print '==> Donwloading : ' + ep
    wget.download(ep,ep_filename)
    down_ep_f.write(ep + '\n')

down_ep_f.close()

if os.path.isfile(pod_ep_file):
	os.remove(pod_ep_file)

####################################################################################
# Update MPD DB
####################################################################################

print '==> Updating DB'

client = MPDClient()
client.connect(mpd_client, mpd_port)
client.update(pod_uri)
client.close()


####################################################################################
# Write Playlist File
####################################################################################

all_files = [f for f in os.listdir(pod_full_dir) if pod_nick in f]
all_files.sort(reverse=True)

f_dates = []
f_temp = []
f_all = []

for f in all_files:
	f_date = f.split('-')[1]
	
	if not (f_date in f_dates):
		f_temp.sort()
		f_all = f_all + f_temp
		f_temp =[]
		f_temp.append(f)
		f_dates.append(f_date)
	else:
		f_temp.append(f)

f_temp.sort()
f_all = f_all + f_temp

print '==> Writing Playlist'

pl_f = open(playlist_file,'w')

f_num = 0
for f in f_all:
  f_uri = pod_uri + '/' + f
  if f_num < max_pl_files:
  	pl_f.write(f_uri + '\n')
  f_num = f_num + 1

pl_f.close()


  			

					
