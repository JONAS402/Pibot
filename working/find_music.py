# prints all albums and bands to lists in music.py
# V0.9
# TODO
# add tracks from albums
"""
find dicts and lists from pathwalking a directory and assigning
the folders to corresponding lists eg:
root/
    artist/
            album/
                contents.mp3


artists = ['band1', 'band2', 'band3']
band1 = ['album1', 'album2', 'album3']
band3 = ['album1', 'album2', 'album3']
band2 = ['album1', 'album2', 'album3']
album = {"01": "track1", "02": "track2", "03": "track3"}

and make and append a module for music
"""


def find_music(directory):
    import os
    ARTISTS = []
    ALBUMS = []
    # src = 'src'  # source folder
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            full = os.path.join(root, name)
            if name.endswith('.m4a'):
                m4a = full.split("/")
                m4a_reverse = m4a[::-1]
                m4a_track, m4a_album, m4a_artist, *junk1 = m4a_reverse
                print("line is artist: {2}, album: {1}, trackname: {0} ".format(m4a_track, m4a_album, m4a_artist))
                if m4a_artist not in ARTISTS:
                    print('adding: ', m4a_artist)
                    ARTISTS.append(m4a_artist)
                    if m4a_album not in ALBUMS:
                        print('adding: ', m4a_album)
                        ALBUMS.append(m4a_album)
                    else:
                        pass
                        # print("album '{0}' by artist '{1} already in list".format(m4a_album, m4a_artist))
                else:
                    # print("artist '{0}' already in list".format(m4a_artist))
                    if m4a_album not in ALBUMS:
                        print('adding: ', m4a_album)
                        ALBUMS.append(m4a_album)
                    else:
                        pass
                        # print("album '{0}' by artist '{1}' already in list".format(m4a_album, m4a_artist))
            elif name.endswith('.mp3'):
                mp3 = full.split("/")
                mp3_rev = mp3[::-1]
                mp3_track, mp3_album, mp3_artist, *junk = mp3_rev
                print("line is artist: {2}, album: {1}, trackname: {0} ".format(mp3_track, mp3_album, mp3_artist))
                if mp3_artist not in ARTISTS:
                    print('adding: ', mp3_artist)
                    ARTISTS.append(mp3_artist)
                    if m4a_album not in ALBUMS:
                        print('adding: ', mp3_album)
                        ALBUMS.append(mp3_album)
                    else:
                        pass
                        # print("album '{0}' by artist '{1}' already in list".format(mp3_album, mp3_artist))
                else:
                    # print("artist '{0}' already in list".format(mp3_artist))
                    if mp3_album not in ALBUMS:
                        print('adding: ', mp3_album)
                        ALBUMS.append(mp3_album)
                    else:
                        pass
                        # print("album '{0}' by artist '{1} already in list".format(mp3_album, mp3_artist))
    literal1 = repr(ARTISTS)
    literal = repr(ALBUMS)
    print('Writing Artists to music.py')
    print('Writing ALBUMS to music.py')
    # music_file = os.path.join(src, 'music.py')
    music_file = 'music.py'
    if os.path.isfile(music_file):
        with open(music_file, 'w') as f:
            f.write("ARTISTS = " + literal1 + '\n\n')
            f.write("ALBUMS = " + literal + '\n\n')
            f.close()
    else:
        print(music_file, 'does not exist, creating now...')
        with open(music_file, 'w') as f:
            f.write("ARTISTS = " + literal1 + '\n\n')
            f.write("ALBUMS = " + literal + '\n\n')
            f.close()

dir1 = '/home/jonas/Music'
find_music(dir1)
