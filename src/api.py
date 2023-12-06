import os
import requests

class LastFmAPI:
    def __init__(self):
        self.api_key = os.getenv('LAST_FM_API_KEY')
        self.base_url = "http://ws.audioscrobbler.com/2.0/"

    def get_user_history(self, username):
        params = {
            'method': 'user.getrecenttracks',
            'user': username,
            'api_key': self.api_key,
            'format': 'json'
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            history = response.json()
            for track in history['recenttracks']['track']:
                track['tags'] = self.get_track_tags(track['artist']['#text'], track['name'])
            return history
        else:
            return None

    def get_track_tags(self, artist, track):
        params = {
            'method': 'track.getTopTags',
            'artist': artist,
            'track': track,
            'api_key': self.api_key,
            'format': 'json'
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            tags = response.json()
            if 'toptags' in tags and 'tag' in tags['toptags']:
                return [tag['name'] for tag in tags['toptags']['tag']]
            else:
                return []
        else:
            return []
