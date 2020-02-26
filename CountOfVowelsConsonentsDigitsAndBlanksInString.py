#Find number of vowels, consonants, digits and blank spaces in a string

consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z',
              'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
consonant_count = 0
vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
vowel_count = 0
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
digit_count = 0
blank_count = 0 

input_string = input("Enter a string: ")

for char in range(0, len(input_string)):
    for c in range(0, len(consonants)):
        if input_string[char] == consonants[c]:
            consonant_count += 1
    for v in range(0, len(vowels)):
        if input_string[char] == vowels[v]:
            vowel_count += 1
    for d in range(0, len(digits)):
        if input_string[char] == str(digits[d]):
            digit_count += 1
    if input_string[char] == ' ':
            blank_count += 1

print("Number of Consonants in string is........: ", consonant_count)
print("Number of Vowels in string is............: ", vowel_count)
print("Number of Digits in string is............: ", digit_count)
print("Number of Blanks in string is............: ", blank_count)
print("Number of Special Characters in string is: ", len(input_string)
                                                  - (consonant_count +
                                                     vowel_count +
                                                     digit_count +
                                                     blank_count))
