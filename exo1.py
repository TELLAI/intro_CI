def reverse(word):
    list_word = list(word)[::-1]
    reverse_word = ""
    for i in list_word:
        reverse_word += i
    return reverse_word

print(reverse("simplon"))
