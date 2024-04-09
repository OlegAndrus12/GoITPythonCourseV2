# store all vowels "aeiou"


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
