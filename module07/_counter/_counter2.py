from collections import Counter


def is_anagram(word1, word2):
    """Checks whether the words are anagrams.

    word1: string
    word2: string

    returns: boolean
    """
    return Counter(word1) == Counter(word2)


res = is_anagram("asds", "sads")
print(res)
