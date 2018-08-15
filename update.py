#!/usr/bin/python2.7

import sys, os
import wget
from mpd import MPDClient
from globals import global_values,pod_dirs,ep_dirs,pod_file_patterns,playlist_max_files

pod_nick_str = ' [ '

for pdir in pod_dirs:
	pod_nick_str = pod_nick_str + pdir + ' | '

for pdir in ep_dirs:
	pod_nick_str = pod_nick_str + pdir + ' | '

pod_nick_str = pod_nick_str.rstrip(' |') + ' ]'

if len(sys.argv) < 2:
  print '[ERROR] Uso: python2.7 ' + sys.argv[0] + pod_nick_str
  sys.exit(2)

pod_nick = sys.argv[1]

if (pod_nick in pod_dirs):
	pod_dir = pod_dirs[pod_nick]
elif (pod_nick in ep_dirs):
	pod_dir = ep_dirs[pod_nick]
else:
  	print '[ERROR] No existe el podcast [' + pod_nick + ']'
  	sys.exit(2)

pod_file_pattern = pod_file_patterns[pod_nick]

pod_full_dir = global_values['base_pod_path'] + '/' + pod_dir

pod_uri = global_values['base_pod_uri_path'] + '/' + pod_dir
playlist_file = global_values['playlist_base_path'] + '/' + pod_dir + '.m3u'

mpd_client = global_values['mpd_client']
mpd_port = global_values['mpd_port']

max_pl_files = playlist_max_files[pod_nick]


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

all_files = [f for f in os.listdir(pod_full_dir) if pod_file_pattern in f]

if pod_nick in ['mesa','facil','locos','play']:
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

else:
	f_all = all_files
	f_all.sort(reverse=True)

print '==> Writing Playlist'

pl_f = open(playlist_file,'w')

f_num = 0
for f in f_all:
  f_uri = pod_uri + '/' + f
  if f_num < max_pl_files:
  	pl_f.write(f_uri + '\n')
  f_num = f_num + 1

pl_f.close()
