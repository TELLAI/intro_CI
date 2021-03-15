def duplicate(liste_test):
    list_dup = []
    for ii, i in enumerate(liste_test):
        jj = ii + 1
        if jj < len(liste_test) - 1:
            for j in liste_test[jj:]:
                if i == j:
                    list_dup.append(i)

    return list_dup

