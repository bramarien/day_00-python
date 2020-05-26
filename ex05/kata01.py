languages = {
                'Python': 'Guido van Rossum',
                'Ruby': 'Yukihiro Matsumoto',
                'PHP': 'Rasmus Lerdorf',
            }


def aff01(languages):
    for fill in languages.items():
        print("%s was created by %s" % (fill))


aff01(languages)
