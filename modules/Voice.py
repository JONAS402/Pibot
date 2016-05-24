# V1.2
# TODO
# clean code
from pyglet.gl import *
from gtts import gTTS
import time
import os
import pyglet
vocab = 'modules/vocab'


def speak(word):
    try:
        tts = gTTS(word, lang='en')
        text = os.path.join(vocab, word)
        tts.save(text + '.mp3')
        time.sleep(1)
    except ConnectionError:
        print('cant say the word', word)


def second_language(word, lang):
    try:
        tts = gTTS(word, lang)
        text = os.path.join(vocab, word)
        tts.save(text + '.mp3')
        time.sleep(1)
    except ConnectionError:
        print('cant say the word', word)


def exit_callback(df):   # do not delete df
    pyglet.app.exit()
    print()


def say(word):
    filepath = os.path.join(vocab, word)
    path_and_name = filepath + '.mp3'
    full_path_name = os.path.realpath(path_and_name)
    loaded_file = pyglet.media.load(full_path_name)
    pyglet.resource.reindex()
    loaded_file.play()
    print("saying... '%s' " % word)
    pyglet.clock.schedule_once(exit_callback, loaded_file.duration)
    pyglet.app.run()


def think(word):
    think_file_path = os.path.join(vocab, word)
    if os.path.isfile(think_file_path + '.mp3'):
        # print("Sentence '%s' is in vocabulary" % word)
        say(word)
    else:
        print("learning to say: '%s' " % word)
        speak(word)
        say(word)


def think2nd(word, lang):
    second_language_think = os.path.join(vocab, word)
    if os.path.isfile(second_language_think + '.mp3'):
        # print("Sentence '%s' is in vocabulary" % word)
        say(word)
    else:
        print("learning to say: '%s' " % word)
        second_language(word, lang)
        say(word)
# USAGE:
# word = input('enter text: ')
# think('howdy')
