import time
# V1.0
# imports all modules for runtime
# needs adding to runtime on next update


def make_directory():
    vocab = 'vocab'
    import os
    if not os.path.exists(vocab):
        print('Making Directory: ', vocab)
        os.makedirs(vocab)
    else:
        print('Directory Exists.')

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
