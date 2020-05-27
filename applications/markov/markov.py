import random

database = {}

# Read in all the words in one go
with open("input.txt") as f:

    words = f.read()
    list_of_words = words.split()
    for i in range(0, len(list_of_words) - 1):
        word = list_of_words[i]
        if word in database:
            database[word].append(list_of_words[i + 1])
        else:
            database[word] = []
            database[word].append(list_of_words[i + 1])

# TODO: analyze which words can follow other words

# TODO: construct 5 random sentences


def add_word(next_word, result):
    new_word = random.choice(database[next_word])
    result += new_word

    # if the next word ends with a period, stop
    if new_word[-1] == "." or new_word[-1] == "?" or new_word[-1] == "!":
        print(result)
        print()
        print()
        return
    # else add a space and keep going
    else:
        result += " "
        add_word(new_word, result)


def make_sentences():
    for i in range(0, 5):
        result = ""
        # get a random word that starts with a capital
        while True:
            starting_word = random.choice(list_of_words)

            if starting_word[0].isupper():
                break
        # add it to the result

        result += starting_word
        result += " "
        add_word(starting_word, result)

        # get the next word


print(make_sentences())

