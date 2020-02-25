#A sample password strenght analysis
good_password = False
while (good_password == False):
    password = input("Enter a password: ")
    if (len(password) < 7):
        print("password should be at least 7 char long")
    elif (password.isalpha()):
        print("Please use special number(s) and special character(s) to make a strong password")
    elif password.isnumeric():
        print("Please use character(s) and special charater(s) to make your password strong")
    else:
        print("Good Going! You have a created a strong password!")
        good_password = True
