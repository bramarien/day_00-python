import sys


def whois(listarg):
    num = listarg[1]
    if len(listarg) > 2:
        print("ERROR")
    elif num.isnumeric() == 0:
        print("ERROR")
    elif num == 0:
        print("I'm Zero.")
    elif (int(num) % 2) == 0:
        print("I'm Even.")
    elif (int(num) % 2) != 0:
        print("I'm Odd.")


whois(sys.argv)
