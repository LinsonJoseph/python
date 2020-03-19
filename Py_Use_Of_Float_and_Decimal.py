#It is not advisable to use float values for cash calculations
#Check this example

a = .1 + .1 + .1 -.3
print("Adding .1 + .1 + .1 - .3 as float values gives the sum as:  ", a)

print()
b = 1.1 + 2.1 + 3.1 - 5.3
print("Adding 1.1 + 2.1 + 3.1 - 5.3 as float values gives the sum as:  ", b)

print()
from decimal import * #an asterix imports all
a = .1 + .1 + .1 -.3
print("Adding .1 + .1 + .1 - .3 as float and converting to decimal gives the sum as:  ", Decimal(a))

print()
x = Decimal('.1')
y = Decimal('.3')
print("Adding .1 + .1 + .1 - .3 as decimal values gives the expected sum as:  ", x + x + x - y)

print()
a = .1 + .1 + .1
print("Adding .1 + .1 + .1 as float values and on conversion to decimal gives the sum as:  ", Decimal(a))

print()

x = Decimal('.1')
y = Decimal('.3')
print("Adding .1 + .1 + .1 - .3 as decimal values gives the sum as:  ", x + x + x - y)
