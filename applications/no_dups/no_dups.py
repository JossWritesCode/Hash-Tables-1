# # No Duplicates

# Input: a string of words separated by spaces. Only the letters `a`-`z`
# are utilized.

# Output: the string in the same order, but with subsequent duplicate
# words removed.

# There must be no extra spaces at the end of your returned string.

# The solution must be `O(n)`.
import re


def no_dups(s):
    database = {}
    s = s.lower()
    s = s.strip()
    re.sub(r"[^\w\d'\s]+", '', s)
    split_sentence = s.split()
    mylist = split_sentence
    mylist = dict.fromkeys(mylist)
    result = []
    for key in mylist:
        result.append(key)
    return ' '.join(result)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
