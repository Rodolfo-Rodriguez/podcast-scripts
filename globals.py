# Valores Globales

global_values = {'base_pod_path':'/mnt/MPD/USB/WD-500/Podcasts',
                  'base_music_path':'/mnt/MPD/USB/WD-500/Music',
                  'base_pod_uri_path':'USB/WD-500/Podcasts',
                  'base_music_uri_path':'USB/WD-500/Music',
                  'playlist_base_path':'/var/lib/mpd/playlists',
                  'ep_base_url':'http://the2rods.com:8080/Feeds',
                  'local_feed_file':'.podcast.xml',
                  'local_ep_file':'.episodes.txt',
                  'down_ep_file':'.downloaded_episodes.txt',
                  'pods_to_filter':['dearriba','justicia','todo','lamesa'],
                  'mpd_client':'localhost',
                  'mpd_port':'6600'}

# Directorios para los episodios de AWS

ep_dirs = {'mesa':'Mesa',
          'locos':'Locos',
          'facil':'Facil',
          'play':'Play'}

# Directorios para los Podcasts

pod_dirs = {'dearriba':'DeArriba',
            'justicia':'Justicia',
            'todo':'Todo',
            'venganza':'Venganza',
            'astroblog':'Astroblog',
            'coffeebreak':'CoffeeBreak',
            'electronicgroove':'ElectronicGroove',
            'djtintin':'DJTintin',
            'dsoh':'DSOH',
            'puromac':'PuroMac',
            'lamesa':'DelSol/LaMesa'}

# Feeds de los Podcasts

pod_urls = {'dearriba':'https://www.oceano.uy/api/podcast.php',
            'justicia':'https://www.oceano.uy/api/podcast.php',
            'todo':'https://www.oceano.uy/api/podcast.php',
            'venganza':'https://venganzasdelpasado.com.ar/posts.rss',
            'astroblog':'http://www.astroblog.cl/feed/',
            'coffeebreak':'https://www.ivoox.com/coffee-break-senal-ruido_fg_f1172891_filtro_1.xml',
            'electronicgroove':'http://www.electronicgroove.com/Podcast/podcast.rss',
            'dsoh':'http://feeds.deepershades.net/dsoh',
            'puromac':'http://feeds.5by5.tv/puromac',
            'lamesa':'https://delsol.uy//feed/lamesa'}

# Filtros para el Titulo del Episodio -> Debe estar para ser incluido

pod_titles = {'dearriba':'De Arriba un Rayo',
              'justicia':'Justicia Infinita',
              'todo':'Todo Pasa',
              'lamesa':'Programa del'}

# Filtros para el Playlist -> El texto debe estar en el archivo

pod_file_patterns = {'mesa':'mesa',
                    'locos':'locos',
                    'facil':'facil',
                    'play':'play',
                    'dearriba':'dearriba',
                    'justicia':'justicia',
                    'todo':'todo',
                    'venganza':'mp3',
                    'astroblog':'mp3',
                    'coffeebreak':'mp3',
                    'electronicgroove':'mp3',
                    'djtintin':'mp3',
                    'dsoh':'mp3',
                    'puromac':'mp3',
                    'lamesa':'mp3'}

# Cantidad Maxima de Episodios en el Playlist

playlist_max_files = {'mesa':15,
          'locos':15,
          'facil':15,
          'play':100,
          'justicia':15,
          'dearriba':15,
          'todo':15,
          'venganza':15,
          'astroblog':200,
          'coffeebreak':15,
          'electronicgroove':100,
          'djtintin':100,
          'dsoh':100,
          'puromac':100,
          'lamesa':10}

# Artist Tags

artist_tags = {'mesa':'Mesa de los Galanes',
              'locos':'Locos por el Futbol',
              'facil':'Facil Desviarse',
              'dearriba':'De Arriba Un Rayo',
              'justicia':'Justicia Infinita',
              'todo':'Todo Pasa',
              'venganza':'La Venganza Sera Terrible',
              'astroblog':'Astroblog',
              'coffeebreak':'Coffee Break',
              'electronicgroove':'Electronic Groove',
              'djtintin':'DJ Tintin',
              'dsoh':'Deeper Shades of House',
              'puromac':'Puro Mac',
              'lamesa':'Mesa de los Galanes'}

