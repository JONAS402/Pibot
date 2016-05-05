# V1.55
# TODO
# set var for cwd and use to export to other modules to use as the root for resource file calls
# add startup

class Runtime:
    # noinspection PyMethodParameters
    def run(key):
        print('Initializing A.I...')  # WRITING STARTUP SCRIPT
        import time
        start = time.ctime()
        try:
            from modules.Voice import think
        except ImportError:
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
                    from modules.diagnostics import run_diagnostics  # TEMP IMPORTS, DEFINE A TRY EXCEPT IMPORT SYSTEM
                    print('running diagnostics')
                    run_diagnostics()
                elif key == 'TRANSLATE':
                    print('broken')
                    from modules.translator import translator
                    text_to_translate = input('enter text to translate: ')
                    translator(text_to_translate)
                elif key == 'MORSECODE':
                    from modules.Morsecode import morsecode
                    convert_to_morsecode = input('enter text to convert to morsecode: ')
                    morsecode(convert_to_morsecode)
                elif key == 'WEBCAM':
                    from modules.webcam import webcam_detect
                    print('webcam is currently in beta--- doesnt kill webcam after grab')
                    webcam_detect()
                elif key == 'FACE':
                    from modules.face_detect import face_detect
                    print('face detect is currently in beta WONT TAKE FILE FROM OTHER FOLDERS')
                    # imagePath = input('enter a file to face detect: ')
                    imagePath = 'modules/src/abba.png'
                    face_detect(imagePath)
                elif key == 'CHAT':
                    from modules.chatbot_client import client
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
