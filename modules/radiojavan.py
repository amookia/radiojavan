import requests
from urllib3.exceptions import InsecureRequestWarning #Avoid SSL warning


class get_audio:
    def __init__(self):
        self.amazon_link = 'https://s3.amazonaws.com/assets.radiojavan.com/app/config/android/config.json'
        self.link = requests.get(self.amazon_link).json()['alt']
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    #get artist name
    def get_artist_mp3s(self,artist_name):
        ret_list = []
        get_mp3 = requests.get(self.link + f'/artist?query={artist_name}',verify = False).json()
        for song in get_mp3['mp3s']:
            ret_list.append({'artist':song['artist'],'song_name':song['song'],'song_link':song['link']
            ,'duration':round(song['duration']/60,2)})
        return ret_list


    #get all mp3's of artist
    def get_artist_name(self,artist):
        artist_names = []
        get_artist = requests.get(self.link + f'/search?query={artist}',verify = False).json()
        for artist in get_artist['artists']:
            artist_names.append({'name':artist['name'],'photo':artist['photo']})
        return artist_names


    def get_album_name(self,name):
        album_names = []
        get_name = requests.get(self.link + f'/artist?query={name}',verify = False).json()
        for data in get_name['albums']:
            album_names.append({'id':data['id'],'album_artist':data['album_artist'],
            'album_name':data['album_album']})
        return album_names

        #get all songs of specific album
    def get_album_mp3(self,id):
        album_data = []
        get_album = requests.get(self.link + f'/mp3?id={str(id)}',verify=False).json()
        for songs in get_album['album_tracks']:
            album_data.append({'artist_name':songs['artist'],'song_name':songs['song']
            ,'song_link':songs['link']})
        return album_data


    def download_track(link,name):
        pass



get_audio = get_audio()
