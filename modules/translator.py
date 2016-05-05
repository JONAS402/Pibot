
# V1.0
# TODO
# MAKE LANGUAGE DICTS, IF SENTENCE NOT IN DICT THEN GOSLATE ELSE SPEAK
LANGUAGES = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Arabic": "ar",
    "Armenian": "hy",
    "Catalan": "ca",
    "Chinese": "zh",
    "Chinese(Mandarin / China)": "zh - cn",
    "Chinese(Mandarin / Taiwan)": "zh - tw",
    "Chinese(Cantonese)": "zh - yue",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "English(Australia)": "en - au",
    "English(UK)": "en - uk",
    "English(US)": "en - us",
    "Esperanto": "eo",
    "Finnish": "fi",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Haitian Creole": "ht",
    "Hindi": "hi",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Indonesian": "id",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Latin": "la",
    "Latvian": "lv",
    "Macedonian": "mk",
    "Norwegian": "no",
    "Polish": "pl",
    "Portuguese": "pt",
    "Portuguese(Brazil)": "pt - br",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian": "sr",
    "Slovak": "sk",
    "Spanish": "es",
    "Spanish(Spain)": "es - es",
    "Spanish(US)": "es - us",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tamil": "ta",
    "Thai": "th",
    "Turkish": "tr",
    "Vietnamese": "vi",
    "Welsh": "cy"
}


def translate(string1, lang):
    from textblob import TextBlob
    try:
        from modules.Voice import think
        from modules.Voice import think2nd
    except ImportError:
        print('import error')
    # print(LANGUAGES[lang])
    x = LANGUAGES[lang]
    try:
        blob = TextBlob(string1)
        var = blob.translate(to=x)
        new_word = str(var)
    except:
        print('Cant think of the words right now... maybe google translate server is down?')
    else:
        # print(new_word)
        think('the sentence')
        think(string1)
        think('is now')
        think2nd(new_word, x)

        think('in')
        think(lang)
        print(" the sentence: ", string1)
        print("is now: ", new_word)
        print("in: ", lang)
        print()


def translator(text_translate):

    print("language choices: ")
    for key in sorted(LANGUAGES.items()):
        print(key[0], end=", ")
    print()
    target_language1 = input('enter language to convert to: ')
    target_language = target_language1.capitalize()

    try:
        translate(text_translate, target_language) # varibles to pass to run.py
    except KeyError:
        print('you need to enter the sub dialect Capitalized')


# USAGE
text_to_translate = 'some text to convert'
# text_to_translate = input('enter text to translate: ')
# translator(text_to_translate)
