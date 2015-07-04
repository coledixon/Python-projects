import ex25

def break_words(stuff):
    words = stuff.splut(' ')
    return words

def sort_sords(words):
    return sorted(words)

def print_first_word(words):
    word.pop(0)
    print(word)

def print_last_word(words):
    word.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return srot_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    prin_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
