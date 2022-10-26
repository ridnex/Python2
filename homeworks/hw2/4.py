char = str(input('Input a letter of the alphabet:'))
vowel = ['a', 'o', 'e', 'u', 'i', 'y']
if char.lower() in vowel:
    print(char, 'is a vowel')
else:
    print(char, 'is a consonant')