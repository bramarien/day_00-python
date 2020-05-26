import sys


MORSE_CODE = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----',
              }


def sos(argv):
    morse = ""
    for arg in argv:
        check = arg.split()
        for word in check:
            if word.isalnum() == 0:
                print("ERROR")
                return
    for arg in argv:
        upper_arg = arg.upper()
        for letter in upper_arg:
            if letter != ' ':
                morse += MORSE_CODE[letter] + ' '
            else:
                morse += '/ '
        if len(argv) > 1 and arg != argv[-1]:
            morse += '/ '
    print(morse)


sys.argv.pop(0)
sos(sys.argv)
