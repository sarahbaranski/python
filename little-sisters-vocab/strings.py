"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return f"un{word}"


def make_word_groups(vocab_words):
    prefix = vocab_words.pop(0)
    
    new_words = [prefix]
    for word in vocab_words:
        new_words.append(prefix + word)
    
    return " :: ".join(new_words)


def remove_suffix_ness(word):
    word = word.split("ness")[0]

    if word[-1] == "i":
        return word[:-1] + "y"
   
    return word
    


def adjective_to_verb(sentence, index):
    
    words = sentence.split(" ")

    if index in (len(words) -1, -1):
        words[index] = words[index][:-1]

    return words[index] + "en"
