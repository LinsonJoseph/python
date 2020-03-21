#Dictionary of (x, x*x) values of numbers from 1 to n where n is an user input

#import numpy to use arange numpy funtion that allows float values
import numpy as np

output_dict = {}
one_to_n = .1
is_Numeric = False
rerun = 'y'

while(is_Numeric == False):
    try:
        one_to_n = float(input("Input a number: "))
        print(one_to_n)
        for i in np.arange(1, one_to_n, 0.5):
            output_dict.update({i : i*i})
    except:
        print("You have not entered a number!")
        is_Numeric = False
    else:
        print(output_dict)
        print("Change program logic only if you expected a different output.") 
    finally:
        while(rerun == 'y'):
            rerun = input("Do you wnat to re-run the program (y/Y)?: ")
            print(rerun[0])
            if rerun[0] != 'Y' and rerun[0] != 'y':
                is_Numeric = True
                break
            if rerun[0] == 'Y' or rerun[0] == 'y':
                is_Numeric = False
                break
            
print("Hope you liked the demo! Do come back for more.")
