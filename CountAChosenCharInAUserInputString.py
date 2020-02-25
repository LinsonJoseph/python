#Count a chosen character in an input string
user_string = input("Enter a string: ")
char_to_count = input("Enter a char to count: ")

count_of_char = user_string.count(char_to_count)
print("Count of " + char_to_count + " in the input string is: ", count_of_char)
