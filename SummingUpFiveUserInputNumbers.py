a = 0
x = 1
while(x<=5):
    try:
        n = int(input("Input an integer(" + str(x) +  "): "))
    except ValueError:
        continue
    else:
        a += n    
    print("Sum of current and previous input(s) is: ", a)
        
    x += 1
