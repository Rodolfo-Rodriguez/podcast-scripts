#!/usr/bin/python2.7

import os, sys
import xml.etree.ElementTree as ET
import wget
from mpd import MPDClient
from globals import global_values,pod_dirs,pod_urls,pod_titles

pod_nick_str = ' [ '
for pdir in pod_dirs:
  pod_nick_str = pod_nick_str + pdir + ' | '
pod_nick_str = pod_nick_str.rstrip(' |') + ' ]'

if len(sys.argv) < 2:
  print '[ERROR] Uso: ' + sys.argv[0] + pod_nick_str
  sys.exit(2)

pod_nick = sys.argv[1]

if not(pod_nick in pod_dirs):
  print '[ERROR] No existe el podcast [' + pod_nick + ']'
  sys.exit(2)

pod_dir = pod_dirs[pod_nick]
pod_full_dir = global_values['base_pod_path'] + '/' + pod_dir

feed_url = pod_urls[pod_nick]
feed_file = pod_full_dir + '/' + global_values['local_feed_file']
down_ep_file = pod_full_dir + '/' + global_values['down_ep_file']

if pod_nick in pod_titles:
  pod_title = pod_titles[pod_nick]

pod_uri = global_values['base_pod_uri_path'] + '/' + pod_dir
playlist_file = global_values['playlist_base_path'] + '/' + pod_dir + '.m3u'

mpd_client = global_values['mpd_client']
mpd_port = global_values['mpd_port']

####################################################################################
# Download and parse feed file 
####################################################################################

if os.path.isfile(feed_file):
  os.remove(feed_file)

print "===> Downloading " + feed_url
wget.download(feed_url, feed_file)

down_episodes = [line.rstrip('\n') for line in open(down_ep_file)]

tree = ET.parse(feed_file)
root = tree.getroot()

channel = root[0]

all_items = channel.findall('item')
pod_items = []

for item in all_items:
  if pod_nick in ['dearriba','justicia','todo']:
    title = item.find('title').text
    guid = item.find('guid').text
    if (pod_title in title) and ('programaentero' in guid):
      pod_items.append(item)
  else:
    pod_items.append(item)

####################################################################################
# Check Downloaded Episodes
####################################################################################

down_ep_f = open(down_ep_file,'a')

print '\n'
print '===================================================================================================='
print 'New Episodes'
print '----------------------------------------------------------------------------------------------------'

for item in pod_items:
  item_url = item.find('enclosure').get('url')
  if not(item_url in down_episodes):
    print item_url

down_ep_f.close()

print '===================================================================================================='

os.remove(feed_file)
