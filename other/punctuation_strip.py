import string
string1 = "`Come, there's no use in crying like that!' said Alice to" \
          "herself, rather sharply; `I advise you to leave off this minute!'" \
          "She generally gave herself very good advice, (though she very" \
          "seldom followed it), and sometimes she scolded herself so"
translator = str.maketrans({key: None for key in string.punctuation})

s = 'string with "punctuation" inside of it! Does this work? I hope so.'

# pass the translator to the string's translate method.
# print(s.translate(translator))
# x # = string1.translate(None, '`,;:()')
print(string1.translate(translator))
