vowels = ['a', 'e', 'i', 'o', 'u']
# print(vowels.__class__)

# word = "Milliways"
word = input("Provide a word to search for vowels: ")

found = []
# print(len(found))

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for vowel in found:
    print(vowel)

# found.remove(letter)
# found.pop(letter)
# found.extend(found)
# found.insert(0, letter)
