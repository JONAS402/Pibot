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
    text = os.path.join(vocab, word)
    t1 = text + '.mp3'
    infile = os.path.realpath(t1)
    music = pyglet.media.load(infile)
    pyglet.resource.reindex()
    music.play()
    print("saying... '%s' " % word)
    pyglet.clock.schedule_once(exit_callback, music.duration)
    pyglet.app.run()


def think(word):
    path1 = os.path.join(vocab, word)
    if os.path.isfile(path1 + '.mp3'):
        # print("Sentence '%s' is in vocabulary" % word)
        say(word)
    else:
        print("learning to say: '%s' " % word)
        speak(word)
        say(word)


def think2nd(word, lang):
    path1 = os.path.join(vocab, word)
    if os.path.isfile(path1 + '.mp3'):
        # print("Sentence '%s' is in vocabulary" % word)
        say(word)
    else:
        print("learning to say: '%s' " % word)
        second_language(word, lang)
        say(word)
# USAGE:
# word = input('enter text: ')
# think('the sentence')
