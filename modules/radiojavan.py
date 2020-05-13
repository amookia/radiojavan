import requests
from urllib3.exceptions import InsecureRequestWarning #Avoid SSL warning


class get_audio:
    def __init__(self):
        self.amazon_link = 'https://s3.amazonaws.com/assets.radiojavan.com/app/config/android/config.json'
        self.link = requests.get(self.amazon_link).json()['alt']
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        self.rdj_list = []

    #get artist name
    def get_artist_mp3s(self,artist_name):
        ret_list = []
        get_mp3 = requests.get(self.link + f'/artist?query={artist_name}',verify = False).json()
        for song in get_mp3['mp3s']:
            self.rdj_list.append({'artist':song['artist'],'song_name':song['song'],'song_link':song['link']
            ,'duration':round(song['duration']/60,2)})
        return self.rdj_list


    #get all mp3's of artist
    def get_artist_name(self,artist):
        artist_names = []
        get_artist = requests.get(self.link + f'/search?query={artist}',verify = False).json()
        for artist in get_artist['artists']:
            self.rdj_list.append({'name':artist['name'],'photo':artist['photo']})
        return self.rdj_list

    #get all songs of specific album
    def get_album(self,id):

        get_album = requests.get(self.link + f'/mp3?id={str(id)}',verify=False).json()
        for songs in get_album['album_tracks']:
            self.rdj_list.append({'artist_name':songs['artist'],'song_name':songs['song']
            ,'song_link':songs['link']})
        return self.rdj_list



get_audio = get_audio()
