# store all vowels "aeiou"

# https://www.codewars.com/kata/5939ab6eed348a945f0007b2/train/python
def longest_word(string_of_words):
    words = string_of_words.split()
    res = words[0]
    for word in words:
        if len(word) >= len(res):
            res = word
    return res



def find_max_vowels(text):
    vowels = "aeiou"
    # replace consonant with .
    for character in text:
        if character.lower() not in vowels:
            text = text.replace(character, ".")

    chains = text.split(".")
    chains.sort(key=len)
    max_chain = chains[-1]
    return max_chain, len(max_chain)


text = "aevsaefsdsade asds d asd sa  Oleeeeeeeeh"
res = find_max_vowels(text)

print(res)
