def reverse_num(nb):
    word = str(nb)
    list_word = list(word)[::-1]
    reverse_word = ""
    for i in list_word:
        reverse_word += i
    return int(reverse_word)



