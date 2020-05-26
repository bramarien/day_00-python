import sys


def main(listarg):
    string = ""
    for i in reversed(range(len(listarg))):
        if i != 0:
            string += listarg[i][::-1]
        if i > 1:
            string += ' '
    print(string.swapcase())


main(sys.argv)
