from modules.radiojavan import get_audio
import requests

artist = input('Enter artist name : ')

name = get_audio.get_artist_name(artist)
co1 = 0
for names in name:
    co1 += 1
    print('( {} ) / {}'.format(co1,names['name']))
choose_artist = int(input('Please choose artist : '))

det = get_audio.get_artist_mp3s(name[choose_artist - 1]['name'])
if len(det) == 0: print('Dada esmo eshtaba zadi') ; exit()
count = 0
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
if quality == 2 : song_link == song_link.replace('/mp3-256/','/mp3-320/')
print('\n\n\nStart downloading {}'.format('  | ' + artist + ' ' + song_name + ' |'))
download = requests.get(song_link)
with open(artist + ' ' + song_name + '.mp3', 'wb') as mp3file:
    mp3file.write(download.content)
print(f'\n\n\n{artist} {song_name} Downloaded successfully')
