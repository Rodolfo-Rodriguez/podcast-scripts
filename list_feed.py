#!/usr/bin/python2.7

import os, sys
import xml.etree.ElementTree as ET
import wget

if len(sys.argv) < 2:
  print '[ERROR] Uso: ' + sys.argv[0] + ' <feed-url>'
  sys.exit(2)

feed_url = sys.argv[1]
feed_file = '.temp_feed.xml'

####################################################################################
# Download and parse feed file 
####################################################################################

if os.path.isfile(feed_file):
  os.remove(feed_file)

print "===> Downloading " + feed_url
wget.download(feed_url, feed_file)

tree = ET.parse(feed_file)
root = tree.getroot()

channel = root[0]

pod_items = channel.findall('item')

print '\n'
print '========================================================================================'
print 'Episodes'
print '========================================================================================'

item_num = 1
for pod_item in pod_items:
  title = pod_item.find('title').text
  pub_date = pod_item.find('pubDate').text
  pod_url = pod_item.find('enclosure').get('url')
  print '[' + str(item_num) + '] - ' + pub_date + ' - ' + title + ' - ' + pod_url
  item_num = item_num + 1

os.remove(feed_file)
