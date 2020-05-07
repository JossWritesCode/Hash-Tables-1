import re



def word_count(s):
    database = {}
    s = s.lower()
    s = s.strip()
    re.sub(r"[^\w\d'\s]+", '', s)
    split_sentence = s.split()
    for word in split_sentence:
        if word in database:
            database[word] += 1
        else:
            database[word] = 1
    return database


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
