#import platform to help print the version of Python the user is running
import platform

#------------------------------------------------------------------------------------------------
#You may assign multiple variable in one line (however, it makes reading the code tough)
programmer = 'Programmer!'; welcome_programmer = 'Hello, {}'.format(programmer)
print(welcome_programmer, 'You are running Python version {}'.format(platform.python_version()))

#------------------------------------------------------------------------------------------------
#Another way of writing this code in Python 3.6 and above is: 
programmer = ' Programmer'
greet_programmer = f'Hello,{programmer}'

version = platform.python_version()
print(welcome_programmer, f'You are running Python version {version}')

#------------------------------------------------------------------------------------------------
