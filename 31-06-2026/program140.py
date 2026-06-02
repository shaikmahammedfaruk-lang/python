def mapping(letters):
	result = {}
	for letter in letters:
		result[letter] = letter.upper()
	return result
print(mapping(["a", "b", "c"]))
print(mapping(["d", "e", "f", "g"]))
print(mapping(["h", "i", "j", "k", "l", "m"]))
