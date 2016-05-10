# Music Crawler (only works with single albums in artist directory)
#   V1.1

def music_crawl(directory):
    import os
    holding_dict = {}
    for root, dirs, files in os.walk(directory, topdown=False):
        for track_name_and_number in files:
            root_split = root.split('/')
            root_split_reversed = root_split[::-1]
            album, band, *waste = root_split_reversed

            if track_name_and_number.endswith('.mp3'):
                # print('root', root)
                print("Artist: {1}, Album: {0}   Track name: {2}".format(album, band, track_name_and_number))
                track_name_and_number_split = track_name_and_number.split(" ", 1)
                track_number = (track_name_and_number_split[0])
                track_name = (track_name_and_number_split[1])
                holding_dict[track_number] = track_name
            elif track_name_and_number.endswith('.m4a'):
                print("Artist: {1}, Album: {0}   Track name: {2}".format(album, band, track_name_and_number))
                track_name_and_number_split = track_name_and_number.split(" ", 1)
                track_number = (track_name_and_number_split[0])
                track_name = (track_name_and_number_split[1])
                holding_dict[track_number] = track_name

        literal = repr(holding_dict)
        full_album = [" '", album, "', ", literal]
        empty_string = ''.join(full_album)
        # if album not in band dir then print band name on new line with collection
        collection = [band, " = [", empty_string, "]\n"]
        collection1 = ''.join(collection)

    with open("my_dict_test.py", "w") as f:
        print(collection1, file=f)

dir1 = '/home/jonas/musictest'
music_crawl(dir1)


