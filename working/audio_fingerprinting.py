#!/usr/bin/python
# V1.0
# python 2.7 only
# no file errors in pycharm, works ok from terminal
# fingerprint whole files allows you to be able to recognise from microphone at any point in the song
# TODO
# write as a functions and pad out more

import warnings
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

password = raw_input('enter mysql password: ')
config = {
     "database": {
         "host": "127.0.0.1",
         "user": "root",
         "passwd": password,
         "db": "dejavu",
     },
     "fingerprint_limit": None  # number of seconds to finger print (None is whole file)
 }

if __name__ == '__main__':
    # scan directory
    djv = Dejavu(config)
    # djv.fingerprint_directory("architects/Lost Forever Lost Together", [".mp3"], 3)  # 3 is processes


# recognise mp3
    song = djv.recognize(FileRecognizer, "/home/jonas/Downloads/dejavu/CC.mp3")
    print("found song '%s\n'" % song)
"""
    # recognise microphone
    # djv = Dejavu(config)
    secs = 10
    song = djv.recognize(MicrophoneRecognizer, seconds=secs)
    if song is None:
        print "Nothing recognized -- did you play the song out loud so your mic could hear it? :)"
    else:
        print "From mic with %d seconds we recognized: %s\n" % (secs, song)
"""
