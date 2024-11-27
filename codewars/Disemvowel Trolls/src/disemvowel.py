def disemvowel(sentence):
    vowels = ["a", "e", "i", "o","u", "A", "E", "I", "O", "U"]
    result = ""
    for letter in sentence:
        if letter not in vowels:
            result += letter
    return result