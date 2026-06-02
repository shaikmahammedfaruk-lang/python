def is_isogram(word):
    word = word.lower()
    # Create a set to store unique letters in the word
    unique_letters = set()
    for letter in word:
        # If the letter is already in the set, it's not an isogram
        if letter in unique_letters:
            return False
        # Otherwise, add it to the set
        unique_letters.add(letter)
    return True
print(is_isogram("Algorism"))
print(is_isogram("PasSword"))
