import string


def text_count(txt):
    upper = 0
    lower = 0
    ponc = 0
    space = 0
    punctation = string.punctuation
    for i in txt:
        if i.islower() == 1:
            lower += 1
        elif i.isupper() == 1:
            upper += 1
        elif i == ' ':
            space += 1
        elif i in punctation:
            ponc += 1
    print("The text contains ", len(txt), " characters:")
    print("- ", upper, " upper letters")
    print("- ", lower, " lower letters")
    print("- ", ponc, " punctation marks")
    print("- ", space, " spaces")


def text_analyzer(*args):
    if len(args) > 1:
        print("ERROR")
    elif len(args) == 0:
        line = input("What is the text to analyse?\n")
        text_count(line)
    elif len(args) == 1:
        text_count(args[0])
