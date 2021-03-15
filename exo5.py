import string
from statistics import mean
def count_word(text):
    phrase = text.split()
    list_count = []
    list_ponct = list(string.punctuation)
    for ii, i in enumerate(phrase):
        count = 0
        for j in i:
            if j not in list_ponct:
                count += 1
        if count > 0:
            list_count.append(count)

    moy = mean(list_count)
    return round(moy, 1)


print(count_word("Ici, c'est Simplon !! "))

