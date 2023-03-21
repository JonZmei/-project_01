def remove_word_with_one_em(s):
    words = s.split()
    result_words = []
    for word in words:
        if word.count("!") != 1:
            result_words.append(word)
    return " ".join(result_words)
print(remove_word_with_one_em("Hi!")) # ""
print(remove_word_with_one_em("Hi! Hi!")) # ""
print(remove_word_with_one_em("Hi! Hi! Hi!")) # ""
print(remove_word_with_one_em("Hi Hi! Hi!")) # "Hi"
print(remove_word_with_one_em("Hi! !Hi Hi!")) # ""
print(remove_word_with_one_em("Hi! Hi!! Hi!")) # "Hi!!"
print(remove_word_with_one_em("Hi! !Hi! Hi!")) # "!Hi!"