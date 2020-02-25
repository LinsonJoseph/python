#Capitalize name input
re_enter = 'Y'
name_split = []
name_capitalized = ''

while(re_enter == 'Y' or re_enter == 'y'):
    name = input("Please enter your name: ")

    name_split = name.split(' ')

    for i in range(0, len(name_split)):
        name_capitalized = name_capitalized + name_split[i].capitalize() + ' ' 

    print("Your name formatted with capitals is: ", name_capitalized)
    name_capitalized = ''
    re_enter = input("\nDo you want to enter another name (Y/(N or other))? ")
    

