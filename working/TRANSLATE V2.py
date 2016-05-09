#  V1.1
# TODO
# INPUT FROM FILE
# ADD VOICE
# define learning program(series of strings fed to every language)
import string
import os
from textblob import TextBlob

"""
problem languages
    "English": "en",
    "English - Australia": "en - au",
    "English - UK": "en - uk",
    "English - US": "en - us",

    "Spanish - Spain": "es - es",
    "Spanish - US": "es - us",
    "Mandarin - Taiwan": "zh - tw",

    "Mandarin - China": "zh - cn",
    """

LANGUAGES = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Arabic": "ar",
    "Armenian": "hy",
    "Brazilian": "pt - br",
    "Catalan": "ca",
    "Chinese": "zh",
    "Cantonese": "zh - yue",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "Esperanto": "eo",
    "Finnish": "fi",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Haitian": "ht",
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
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian": "sr",
    "Slovak": "sk",
    "Spanish": "es",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tamil": "ta",
    "Thai": "th",
    "Turkish": "tr",
    "Vietnamese": "vi",
    "Welsh": "cy"
}

string1 = 'new words for like this'
text = "The titular threat of The Blob has always struck me as the ultimate movie monster an insatiably hungry," \
       " amoeba like mass able to penetrate virtually any safeguard, capable of as a doomed doctor chillingly" \
       " describes it assimilating flesh on contact. Snide comparisons to gelatin be damned, it's a concept with" \
       " the most devastating of potential consequences, not unlike the grey goo scenario proposed by technological" \
       " theorists fearful of artificial intelligence run rampant."


def problem_words(word_list, language):
    name_lower = language.lower()
    name_upper = name_lower.upper()
    languages = 'languages'
    import_languages_string = languages + '.' + name_lower + '_problem_words'
    path_and_file = os.path.join('languages', name_lower + '_problem_words.py')
    if os.path.isfile(path_and_file):
        try:

            imported = getattr(__import__(import_languages_string, fromlist=[name_upper + "_PROBLEM_WORDS"]), name_upper + "_PROBLEM_WORDS")
            word_split_list = word_list.split(' ')
            for word in word_split_list:
                if word not in imported:
                    print("the word '{0}' is not in the '{1}' problem file".format(word, name_lower))
                    imported.append(word)
                    word_list = repr(imported)
                    with open(path_and_file, "w") as f:
                        print(name_upper + "_PROBLEM_WORDS = " + word_list, file=f)
                else:
                    print("the word '{0}' is in the '{1}' problem file".format(word, name_lower))
        except AttributeError:
            print("problem  with the '{0}' languages file... delete it and try again".format(language))
    else:
        print("creating '{0}' problem word file...".format(language))
        word = word_list.split(' ')
        name_lower = language.lower()
        name_upper = name_lower.upper()
        # new_words_list.append(word)
        new_word_list = repr(word)
        with open(path_and_file, "w") as f:
            print(name_upper + "_PROBLEM_WORDS = " + new_word_list, file=f)

# problem_words('banana balls seven minge praerie biscuit', 'albanian')

def translate_and_learn(some_words, language):
    import os
    lower_language = language.lower()
    path_and_file = os.path.join('languages', lower_language + '.py')
    if os.path.isfile(path_and_file):
        print("'{0} language file exists... continuing...".format(language))
    else:
        print("making '{0}' language file...".format(language))
        language_caps = language.upper()
        with open(path_and_file, "w") as f:
            print(language_caps + " = {}", file=f)
    translate_v2(some_words, language)

# translate_and_learn(text, 'albanian')

# noinspection PyBroadException,PyBroadException
def translate_v2(some_string, input_language):
    language_caps = input_language.capitalize()
    name_lower = input_language.lower()
    name_upper = input_language.upper()
    if os.path.exists('languages'):
        path_and_file = os.path.join('languages', name_lower + '.py')
        if os.path.isfile(path_and_file):
            languages = 'languages'
            import_languages_string = languages + '.' + str(name_lower)
            imported = getattr(__import__(import_languages_string, fromlist=[name_upper]), name_upper)
            split_string = some_string.split(' ')
            for word in split_string:
                if word not in imported.keys():
                    try:
                        language_value = LANGUAGES[language_caps]
                        word_to_convert = TextBlob(word)
                        translated = word_to_convert.translate(to=language_value)
                        new_word = str(translated)
                        print("the word '{0}' is now '{1}' in '{2}'...".format(word, new_word, language_caps))
                        if new_word not in imported.values():
                            print("adding : '{0}' to dictionary".format(new_word))
                            imported[word] = new_word
                    except:
                        print("problem with word '{0}' ...skipping".format(word))
                        problem_words(word, input_language)

                else:
                    print("'{0}' is in dictionary as '{1}'".format(word, imported[word]))
            word_list = repr(imported)
            with open(path_and_file, "w") as f:
                print(name_upper + " = " + word_list, file=f)
        else:
            print('file doesnt exist')
            translate_and_learn(some_string, input_language)

# translate_v2(string1, 'haitian creole')





def translate_string_to_language(some_text, input_language):
    language_caps = input_language.capitalize()
    name_lower = input_language
    name_upper = name_lower.upper()
    languages = 'languages'
    import_languages_string = languages + '.' + name_lower
    imported = getattr(__import__(import_languages_string, fromlist=[name_upper]), name_upper)
    split_list = some_text.split(' ')
    empty_string = []
    for word in split_list:
        if word not in imported.keys():
            print(word, 'not in dictionary')
            empty_string.append(word)
        else:
            print(word, 'is in dictionary... as...', imported[word])
            converted_word = str(imported[word])
            empty_string.append(converted_word)
    converted_string = ' '.join(empty_string)
    print("'{0}' is now '{1}' in '{2}'".format(some_text, converted_string, language_caps))

#translate_string_to_language(string1, 'german')




def learn_some_basics(file):
    with open(file) as f:
        print("about to learn the contents of the file '{0}' in all languages".format(file))
        contents = f.read()
        # print('contents = ', contents)
        translator = str.maketrans({key: None for key in string.punctuation})
        print(contents.translate(translator))
        for key in sorted(LANGUAGES.items()):
            # print(key[0], end=", ")
            translate_and_learn(contents, key[0])

# file = 'alice in wonderland.txt'
file = 'working/test.txt'
learn_some_basics(file)
