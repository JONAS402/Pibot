#  V1.0
# TODO
# INPUT FROM FILE
# ADD VOICE


string1 = 'new words for like this'
text = "The titular threat of The Blob has always struck me as the ultimate movie monster an insatiably hungry, amoeba like mass able to penetrate virtually any safeguard, capable of as a doomed doctor chillingly describes it assimilating flesh on contact. Snide comparisons to gelatin be damned, it's a concept with the most devastating of potential consequences, not unlike the grey goo scenario proposed by technological theorists fearful of artificial intelligence run rampant."


def translate_v2(some_string, input_language):
    language_caps = input_language.capitalize()
    from textblob import TextBlob
    from modules.translator import LANGUAGES
    import os
    if os.path.exists('languages'):
        path_and_file = os.path.join('languages', input_language + '.py')

        if os.path.isfile(path_and_file):
            name_lower = input_language
            name_upper = name_lower.upper()
            languages = 'languages'
            import_languages_string = languages + '.' + name_lower
            imported = getattr(__import__(import_languages_string, fromlist=[name_upper]), name_upper)
            split_string = some_string.split(' ')
            for word in split_string:
                if word not in imported.keys():
                    try:
                        language_value = LANGUAGES[language_caps]
                        word_to_convert = TextBlob(word)
                        var = word_to_convert.translate(to=language_value)
                        new_word = str(var)
                        print("the word '{0}' is now '{1}' in '{2}...".format(word, new_word, language_caps))
                        if new_word not in imported.values():
                            print("adding : '{0}' to dictionary".format(new_word))
                            imported[word] = new_word
                    except:
                        print("problem with word '{0}' ...skipping".format(word))
                else:
                    print("'{0}' is in dictionary as '{1}'".format(word, imported[word]))
            word_list = repr(imported)
            with open(path_and_file, "w") as f:
                print(name_upper + " = " + word_list, file=f)
        else:
            print('file doesnt exist')

# translate_v2('wash computer window love cup', 'french')


def translate_and_learn(some_words, language):
    import os
    path_and_file = os.path.join('languages', language + '.py')

    if os.path.isfile(path_and_file):
        print("'{0} language file exists... continuing...".format(language))
    else:
        print("making '{0}' language file...".format(language))
        language_caps = language.upper()
        with open(path_and_file, "w") as f:
            print(language_caps + " = {}" , file=f)
    translate_v2(some_words, language)

translate_and_learn(text, 'welsh')


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
        else:
            print(word, 'is in dictionary... as...', imported[word])
            converted_word = str(imported[word])
            empty_string.append(converted_word)
    converted_string = ' '.join(empty_string)
    print("'{0}' is now '{1}' in {2}".format(some_text, converted_string, language_caps))

# translate_string_to_language(string1, 'french')
