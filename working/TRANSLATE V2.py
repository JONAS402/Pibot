#  V1.4
# TODO

# ADD VOICE
import string
import os
from textblob import TextBlob


LANGUAGES = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "American": "en-us",
    "Arabic": "ar",
    "Armenian": "hy",
    "Australian": "en - au",
    "Azerbaijani": "az",
    "Basque": "eu",
    "Belarusian": "be",
    "Bengali": "bn",
    "Bosnian": "bs",
    "Brazilian": "pt-br",  # unicode error
    "Bulgarian": "bg",
    "Burmese": "my",
    "Catalan": "ca",
    "Cebuano": "ceb",
    "Chichewa": "ny",
    "Chinese": "zh",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en-uk",
    "Esperanto": "eo",
    "Estonian": "et",
    "Filipino": "tl",
    "Finnish": "fi",
    "French": "fr",
    "Galician": "gl",
    "Georgian": "ka",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Haitian": "ht",
    "Hausa": "ha",
    "Hebrew": "iw",
    "Hindi": "hi",
    "Hmong": "hmn",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Igbo": "ig",
    "Indonesian": "id",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jw",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Khmer": "km",
    "Korean": "ko",
    "Lao": "lo",
    "Latin": "la",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Macedonian": "mk",
    "Malagasy": "mg",
    "Malay": "ms",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Mandarin": "zh-cn",
    "Maori": "mi",
    "Marathi": "mr",
    "Mongolian": "mn",
    "Nepali": "ne",
    "Norwegian": "no",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian": "sr",
    "Sesotho": "st",
    "Sinhala": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Spanish": "es",
    "Sudanese": "su",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tamil": "ta",
    "Taiwanese": "zh-tw",
    "Tajik": "tg",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Yiddish": "yi",
    "Yoruba": "yo",
    "Zulu": "zu",
}


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
                    print("the word '{0}' is not in the '{1}' problem file...adding...".format(word, name_lower), end='')
                    imported.append(word)
                    word_list = repr(imported)
                    with open(path_and_file, "w") as f:
                        print(name_upper + "_PROBLEM_WORDS = " + word_list, file=f)
                    print("...added", end='\n')
                else:
                    pass
                    # print("the word '{0}' is in the '{1}' problem file".format(word, name_lower))
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
        pass
        # print("'{0} language file exists... continuing...".format(language))
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
            try:
                imported = getattr(__import__(import_languages_string, fromlist=[name_upper]), name_upper)
            except AttributeError:
                print("AttributeError: problem  with the '{0}' languages file... delete it and try again".format(input_language))
                os.remove(path_and_file)
            split_string = some_string.split(' ')
            for word in split_string:
                if word != '':
                    try:
                        if word not in imported.keys():
                            try:
                                language_value = LANGUAGES[language_caps]
                                word_to_convert = TextBlob(word)
                                translated = word_to_convert.translate(to=language_value)
                                new_word = str(translated)
                                # print("the word '{0}' is now '{1}' in '{2}'...".format(word, new_word, language_caps))
                                if new_word not in imported.values():
                                    print("adding : '{0}' to '{1}' dictionary...".format(new_word, language_caps), end='')
                                    imported[word] = new_word
                                    word_list = repr(imported)
                                    with open(path_and_file, "w") as f:
                                        print(name_upper + " = " + word_list, file=f)
                                    print("...added", end='\n')
                            except:
                                # print("problem translating '{0}' into '{1}' ...skipping".format(word, language_caps))
                                problem_words(word, input_language)
                        else:
                            print(
                                "'{0}' is in the '{2}' dictionary as'{1}'".format(word, imported[word], language_caps))
                    except UnboundLocalError:
                        print("UnboundLocalError: problem  with the '{0}' languages file... delete it and try again".format(input_language))
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

# translate_string_to_language(string1, 'german')


def learn_some_basics(file):
    with open(file) as f:
        print("about to learn the contents of the file '{0}' in all languages".format(file))
        content = f.read()
        new_line_stripped = content.replace('\n', ' ')
        zero_width_stripped = new_line_stripped.replace('\u200b', '')             # test
        translator = str.maketrans({key: None for key in string.punctuation})
        translate = new_line_stripped.translate(translator)
        for key in sorted(LANGUAGES.items()):
            translate_and_learn(translate, key[0])
            print("learnt... '{0}'".format(key[0]))
file = 'working/alice in wonderland.txt'
# file = 'working/test.txt'
learn_some_basics(file)
