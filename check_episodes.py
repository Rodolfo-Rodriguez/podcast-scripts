#!/usr/bin/python2.7

import os, sys
import os.path
import xml.etree.ElementTree as ET
import wget
from mpd import MPDClient
from globals import global_values,ep_dirs

#  Baja episodios de las grabaciones de AWS

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


####################################################################################
# Download and parse feed file 
####################################################################################

if os.path.isfile(pod_ep_file):
	os.remove(pod_ep_file)

wget.download(feed_url, pod_ep_file)

down_episodes = [line.rstrip('\n') for line in open(down_ep_file)]
pod_episodes = [line.rstrip('\n') for line in open(pod_ep_file)]

####################################################################################
# Check Downloaded Episodes
####################################################################################

down_ep_f = open(down_ep_file,'a')

print '\n'
print '===================================================================================================='
print 'New Episodes'
print '----------------------------------------------------------------------------------------------------'

for ep in pod_episodes:
  if not(ep in down_episodes):
    print ep

down_ep_f.close()

print '===================================================================================================='

if os.path.isfile(pod_ep_file):
	os.remove(pod_ep_file)

