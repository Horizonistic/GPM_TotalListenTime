#!/usr/bin

from gmusicapi import Mobileclient
from gmusicapi import CallFailure
import json
import pprint
from urllib3.exceptions import HTTPError
from datetime import datetime, date, time, timedelta

api = Mobileclient(debug_logging=False)
logged_in = api.login("bmwssu@gmail.com", "bslwafghqkkjobij", Mobileclient.FROM_MAC_ADDRESS)

songs = api.get_all_songs()

album_info = {}
total = 0

# with open("songs", 'r') as file:
    # songs = json.load(file)
for song in songs:
    if 'playCount' in song and 'durationMillis' in song:
        if song['album'] not in album_info:
            album_info[song['album']] = {song['trackNumber']: (song['playCount'], song['durationMillis'])}
            total += int(song['playCount']) * int(song['durationMillis'])
        else:
            album_info[song['album']].update({song['trackNumber']: (song['playCount'], song['durationMillis'])})
            total += int(song['playCount']) * int(song['durationMillis'])

pprint.pprint(album_info)
pprint.pprint(total)

delta = timedelta(milliseconds=total)

date = datetime.now()

print(delta)