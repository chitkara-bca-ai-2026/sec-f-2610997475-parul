# Lab 10 - Text Processing Tool

# Taking input
sentence = input("Enter a sentence: ")

# Character indexing
position = int(input("Enter position for indexing: "))
print("Character at position", position, ":", sentence[position])

# String slicing
start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing: "))
print("Sliced string:", sentence[start:end])

# Uppercase and lowercase
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

# Replacing a word
old_word = input("Enter word to replace: ")
new_word = input("Enter replacement word: ")
new_sentence = sentence.replace(old_word, new_word)

print("After replacement:", new_sentence)

# Finding length
print("Length of sentence:", len(sentence))

print("\nAnalysis Complete!")