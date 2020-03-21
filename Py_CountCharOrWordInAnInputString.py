#Count a chosen character/word in an input string
user_string = input("\033[1;33;40mEnter a string: ")
count_another = True
 
while count_another == True:
    char_to_count = input("\033[1;35;43mEnter a character/word to count: ")

    count_of_char = user_string.count(char_to_count)
    char_in_UPPER_CASE = char_to_count.upper() 
    count_of_CHAR = user_string.count(char_in_UPPER_CASE)

    print(f"\033[0;37;40mCount of \033[1;35;46m'{char_to_count}'\033[0;37;40m in the input string is - \033[1;35;46m {count_of_char + count_of_CHAR} ")
    repeat = input("\nDo you want to count another character/word?: ")
    response = repeat[0]
    
    if response not in ['y', 'Y', 's', 'S']:
        count_another = False
