t = (19, 42, 21, 12)


def aff00(kata):
    print("The %d numbers are: " % len(kata), end='')
    for i in range(len(kata)):
        print("%d" % kata[i], end='')
        if i != len(kata) - 1:
            print(", ", end='')


aff00(t)
