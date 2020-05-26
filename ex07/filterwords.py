import sys
import string


def filterword(argv):
    if len(argv) != 3 or argv[2].isdigit() == 0:
        print("ERROR")
    else:
        n = int(argv[2])
        line = argv[1]
        for punc in string.punctuation + '→':
            line = line.replace(punc, '')
        clean_word = line.split()
        final_list = []
        for word in clean_word:
            if len(word) > n:
                final_list.append(word)
        print(final_list)


filterword(sys.argv)
