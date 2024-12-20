def single_root_words (root_word, *other_words):
    same_words = []
    root_word = root_word.lower ()
    for elem in other_words:
        if elem.lower() in root_word or root_word in elem.lower():
            same_words.append(elem)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)