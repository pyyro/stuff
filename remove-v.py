'''
removes vowels from a given text 
'''
VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
text = input('Enter your text here: ')


final_text = 'Final Text: ' + ''
removed_vowels = 'Removed Vowels are: ' + ''

for letter in text:
    if letter not in VOWELS:
        final_text += letter

    if letter in VOWELS:
        removed_vowels += letter

print(final_text)
print(removed_vowels)



