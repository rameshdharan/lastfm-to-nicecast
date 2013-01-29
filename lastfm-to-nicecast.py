#!/usr/bin/env python

import pylast
import time
import os
import datetime
import sys

API_KEY = 'REPLACE_WITH_YOUR_API_KEY'
API_SECRET = 'REPLACE_WITH_YOUR_API_SECRET'
LASTFM_USER = 'REPLACE_WITH_YOUR_USER_NAME'

lastfm = pylast.get_lastfm_network(API_KEY, API_SECRET)
user = lastfm.get_user(LASTFM_USER)

while True:
   time.sleep(5)

   try:
      track = user.get_now_playing()
      txt = ("Title: %s\nArtist: %s\nAlbum: %s\nTime: %s\n" %
             (track.get_name(), track.get_artist(), track.get_album().get_title(),
              datetime.timedelta(milliseconds=track.get_duration())))
      print(txt)

      nowplaying = open(os.path.expanduser('~/Library/Application Support/Nicecast/NowPlaying.txt'), 'w')
      nowplaying.write(txt)
      nowplaying.close()

   except AttributeError as ae:
      pass
