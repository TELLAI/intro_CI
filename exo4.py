import string
def count_word(text):
    phrase = list(text)
    count = 0
    list_ponct = list(string.punctuation)
    for ii, i in enumerate(phrase):
        if (phrase[ii - 1] == " " and i not in list_ponct) or (i in list_ponct and ii == (len(phrase) - 1)): 
            count += 1
    return count


