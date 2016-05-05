# V1.0
MORSECODE = {
    "A": ".-", "B": "-...", "C": "-.-.",
    "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----",
    "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--"
}


def morsecode(string1):
    print('original text: ', string1)
    x = string1.upper()
    for let in x:
        if let == ' ':
            print('  ', end='')
        else:
            print(MORSECODE[let], end='')
    print()

# USAGE
# string1 = 'some string to convert to morsecode'
# string1 = input('enter text to convert to morsecode: ')
# morsecode(string1)  # var to pass to run.py
