# V1.0
# TODO
# cant run until os reinstall due to mysql error
# so untested on PIBOT
# write as a function and pad out more

from dejavu import Dejavu
password = input('enter password')
config = {
     "database": {
         "host": "127.0.0.1",
         "user": "root",
         "passwd": "password",
         "db": "dejavu",
     },
     "fingerprint_limit": None  # number of seconds to finger print (None is whole file)
 }
djv = Dejavu(config)
djv.fingerprint_directory("va_us_top_40/mp3", [".mp3"], 3)  # 3 is processes


# after instantating Dejavu
from dejavu.recognize import FileRecognizer
song = djv.recognize(FileRecognizer, "va_us_top_40/wav/Mirrors - Justin Timberlake.wav")

# fingerprint from mic
from dejavu.recognize import MicrophoneRecognizer
song = djv.recognize(MicrophoneRecognizer, seconds=10)  # Defaults to 10 seconds.