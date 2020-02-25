#Print characters in the even places in an input string
string_input = input("Enter a string: ")

def splitstr(input_str):
    return [char for char in input_str]

input_list = splitstr(string_input)

for x in range(1, len(input_list), 2):
    print("The characters in the even spaces are: ", input_list[x])
