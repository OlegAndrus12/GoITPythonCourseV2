def countConsistentStrings(allowed, words):
    count = 0
    allowed = set(allowed)
    for word in words:
        if set(word) == (allowed):
            count += 1
    return count


allowed = "abc"
words = ["a", "b", "c", "ab", "ac", "bc", "abc"]

res = countConsistentStrings(allowed, words)
print(res)
