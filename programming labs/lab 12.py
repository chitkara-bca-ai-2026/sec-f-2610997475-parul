# Lab 12 - Document Analysis System

# Taking input
sentence = input("Enter a sentence: ")

# Initializing counters
words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

# Analyzing each character
for ch in sentence:

    if ch.lower() in "aeiou":
        vowels += 1

    elif ch.isalpha():
        consonants += 1

    elif ch.isdigit():
        digits += 1

    elif ch.isspace():
        spaces += 1

    else:
        special += 1

# Calculating total letters
letters = vowels + consonants

# Calculating vowel percentage
if letters > 0:
    percentage = (vowels / letters) * 100
else:
    percentage = 0

# Displaying report
print("\n================================")
print("       DOCUMENT ANALYSIS REPORT")
print("================================")

print("Sentence:", sentence)
print("Total characters:", len(sentence))

print("\n--- Character Breakdown ---")
print("Words:", words)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

print("\n--- Summary ---")
print("Total letters:", letters)
print(f"Vowel percentage: {percentage:.1f}%")

print("\n================================")
print("Analysis Complete!")
print("================================")