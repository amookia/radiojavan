from modules.radiojavan import get_audio
import requests


artist = input('Enter artist name : ')
name = get_audio.get_artist_name(artist)
co1 = 0
for names in name:
    co1 += 1
    print('( {} ) / {}'.format(co1,names['name']))
choose_artist = int(input('Please choose artist : '))
choose_type = int(input('\n--------------------------\n\n( 1 ) Download track from album\n( 2 ) Download from all tracks\nPlase choose : '))
count = 0
if choose_type == 1:
    print('\n--------------------------\n')
    album = get_audio.get_album_name(name[choose_artist - 1]['name'])
    for alb in album:
        count += 1
        print('( {} ) / {} / {}'.format(count,alb['album_artist'],alb['album_name']))
    #Download
    numse = int(input('Select : '))
    id = album[numse - 1]['id']
    get_album_tracks = get_audio.get_album_mp3(id)
    co2 = 0
    print('\n--------------------------\n')
    for tracks in get_album_tracks:
        co2 += 1
        print('( {} ) / {} / {}'.format(co2,tracks['artist_name'],tracks['song_name']))
    num = int(input('Select :'))
    artist = get_album_tracks[num-1]['artist_name']
    song_name = get_album_tracks[num-1]['song_name']
    song_link = get_album_tracks[num-1]['song_link']

if choose_type == 2:
    det = get_audio.get_artist_mp3s(name[choose_artist - 1]['name'])
    if len(det) == 0: print('Dada esmo eshtaba zadi') ; exit()
    #print all tracks
    for details in det:
        count += 1
        print('( {} ) / {} / {}'.format(count,details['artist'],details['song_name']))

    #Download
    num = int(input('Select : '))
    artist = det[num-1]['artist']
    song_name = det[num-1]['song_name']
    song_link = det[num-1]['song_link']

#Quality
quality = int(input(f'\n( 1 ) {artist} {song_name} | 256\n( 2 ) {artist} {song_name} | 320\nPlease choose : '))
def_quality = '256'
if quality == 2 : song_link == song_link.replace('/mp3-256/','/mp3-320/') ; def_quality = '320'
print('\n\n\nStart downloading {}'.format('  | ' + artist + ' ' + song_name + ' ' + def_quality +  ' |'))
download = requests.get(song_link)
with open(artist + ' ' + song_name + ' ' + def_quality +'.mp3', 'wb') as mp3file:
    mp3file.write(download.content)
print(f'\n\n\n{artist} {song_name} {def_quality} Downloaded successfully')
