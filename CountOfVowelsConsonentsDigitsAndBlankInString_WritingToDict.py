#Find number of vowels, consonants, digits and blank spaces in a string
#----------------------------------------------------------------------

#Define the list for consonants and initialize a varialble for it
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z',
              'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
consonant_count = 0

#Define the list of vowels and initialize a varialble for it
vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
vowel_count = 0

#Define the list of digits and initialize a varialble for it
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
digit_count = 0

#Initialize a variable for computing count of blank spaces
blank_count = 0 

#Define a dictionary to hold the counted values
charCountDictionary = {}

#Get string input from user
input_string = input("Enter a string: ")

#Logic for computing the character count
for char in range(0, len(input_string)):
    for c in range(0, len(consonants)):
        if input_string[char] == consonants[c]:
            consonant_count += 1
    charCountDictionary.update({'Consonant Count': consonant_count})    
    for v in range(0, len(vowels)):
        if input_string[char] == vowels[v]:
            vowel_count += 1
    charCountDictionary.update({'Vowel Count': vowel_count})
    for d in range(0, len(digits)):
        if input_string[char] == str(digits[d]):
            digit_count += 1
    charCountDictionary.update({'Digit Count': digit_count})
    if input_string[char] == ' ':
            blank_count += 1
    charCountDictionary.update({'Blankspace Count': blank_count})
    charCountDictionary.update({'Special Char Count': len(input_string)
                                                  - (consonant_count +
                                                     vowel_count +
                                                     digit_count +
                                                     blank_count)})

#Print the dictionary containg the calculated values
print(charCountDictionary)
