# V1.56
# TODO
# set var for cwd and use to export to other modules to use as the root for resource file calls
# main menu
#

import time
import os


def make_directory():
    vocab = 'modules/vocab'
    if not os.path.exists(vocab):
        print('Making Directory: ', vocab)
        os.makedirs(vocab)
    else:
        print('Directory Exists.')


class Runtime:
    # noinspection PyMethodParameters
    def run(key):
        start = time.ctime()
        print('Initializing A.I...')
        make_directory()
        try:
            print('Importing... Voice')
            from modules.Voice import think
        except ImportError:
            print('error importing: Voice')
            print('cannot initialize A.I...')
            print('exiting...')
            raise SystemExit
        try:
            print('Importing... Morsecode')
            from modules.Morsecode import morsecode
        except ImportError:
            print('error importing: Morsecode')
            print('cannot initialize A.I...')
            print('exiting...')
            raise SystemExit
        try:
            print('Importing... Diagnostics')
            from modules.diagnostics import run_diagnostics
        except ImportError:
            print('error importing: Diagnostics')
            print('cannot initialize A.I...')
            print('exiting...')
            raise SystemExit
        try:
            print('Importing... Translator')
            from modules.translator import translator
        except ImportError:
            print('error importing: Translator')
            print('cannot initialize A.I...')
            print('exiting...')
            raise SystemExit
        try:
            print('Importing... Webcam')
            from modules.webcam import webcam_detect
        except ImportError:
            print('error importing: Webcam')
            print('cannot initialize A.I...')
            print('exiting...')
            raise SystemExit
        try:
            print('Importing... Face Detect')
            from modules.face_detect import face_detect
        except ImportError:
            print('error importing: Face Detect')
            print('cannot initialize A.I...')
            print('exiting...')
            raise SystemExit
        try:
            print('Importing... Chat client')
            from modules.chatbot_client import client
        except ImportError:
            print('error importing: Chat Client')
            print('cannot initialize A.I...')
            print('exiting...')
            raise SystemExit
        else:
            print('A.I Initialized.')
            think("hi, i'm ready to talk")
            key = ''
            KILLSWITCH = 0
            while KILLSWITCH != 1:
                think('please enter some text and i will talk')
                think("enter kill, to kill")
                key = input("Please enter text, 'KILL' to kill: ")
                if key == 'KILL':
                    KILLSWITCH = 1
                elif key == 'DIAG':
                    print('running diagnostics')
                    run_diagnostics()
                elif key == 'TRANSLATE':
                    print('broken')
                    text_to_translate = input('enter text to translate: ')
                    translator(text_to_translate)
                elif key == 'MORSECODE':
                    convert_to_morsecode = input('enter text to convert to morsecode: ')
                    morsecode(convert_to_morsecode)
                elif key == 'WEBCAM':
                    print('webcam is currently in beta--- doesnt kill webcam after grab')
                    webcam_detect()
                elif key == 'FACE':
                    print('face detect is currently in beta WONT TAKE FILE FROM OTHER FOLDERS')
                    # imagePath = input('enter a file to face detect: ')
                    imagePath = 'modules/src/abba.png'
                    face_detect(imagePath)
                elif key == 'CHAT':
                    print('chatbot in beta')
                    print('chatbot may or may not be running')
                    client()
                else:
                    print(key)
                    think(key)
            else:
                print('Kill Command Received, Killing A.I...')
                think('Kill command received, killing A I')
                end = time.ctime()
                print('           ...A.I Is Dead R.I.P....')
                print("Born    ...{0}...".format(start))
                print("Died    ...{0}...".format(end))

ai = Runtime()
ai.run()
