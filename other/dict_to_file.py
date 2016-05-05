import os
dict = {}
str = '01 track1 with lots of spaces.mp3', '02 track2-with-hyphens.mp3', '03 track3_with_under_scores.mp3', '04 track4.mp3', '05 track5.mp3', '06 track6.mp3'
dir = '/home/jonas/musictest'
temp = {}
albums = {}
album1 = []
for root, dirs, files in os.walk(dir, topdown=False):

    # print(files)
    for name in files:
        # print(name)
        x = root.split('/')
        rev = x[::-1]
        album, band, *shit = rev
        if name.endswith('.mp3'):
            # print('root', root)
            # print('dirs', dirs)
            # print("artist {0}, band {1}".format(album, band))

            xz = name.split(" ", 1)
            print('zx =', xz)
            z = (xz[0])
            y = (xz[1])
            temp[z] = y
    literal = repr(temp)
    album1.append(" '")
    album1.append(album)
    album1.append("': ")
    album1.append(literal)
    empty_string = ''.join(album1)
    # if album not in band dir then print band name on new line with collection
    collection = []
    collection.append(band)
    collection.append(" = [")
    collection.append(empty_string)
    collection.append("]\n")
    collection1 = ''.join(collection)
    print('empty_string = ', empty_string)
# print('literal ', literal)
    print('album1 = ', album1)
# print(album + " = " + literal)
with open("my_dict_test.py", "w") as f:
    print(collection1, file=f)


'''
for i in str:
    x = i.split(" ", 1)
    print(x)
    z = (x[0])
    y = (x[1])
    dict[z] = y

print(dict)
literal = repr(dict)
    x = i.split(" ", 1)
    print(x)
    z = (x[0])
    y = (x[1])
    dict[z] = y

print(dict)
literal = repr(dict)

#

print()
print("dict = ", literal)
'''