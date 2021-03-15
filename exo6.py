def palindrom(word):
    word_r = word[::-1]
    rep = "oui"
    for ii, i in enumerate(list(word)):
        if i != list(word_r)[ii]:
            rep = "non"
            return rep
    return rep

