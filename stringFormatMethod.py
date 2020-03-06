#use of the format method on strings

#------------------------------------------ Example 1 - Use of format method --------------------------------------
print("Example 1 - Use of format method")
print("--------------------------------")
planet_input = input("Hi there! Which planet are you from?: ")
capitalized_planet = planet_input.capitalize()

#format method puts the argument it receives inside the curly braces '{}
print('\nHello, {} Geek! We have used "format" and I am a function put in it'.format(planet_input.capitalize()))
print('Hello, {} Guru! We have used "format" and I am a variable put in it'.format(capitalized_planet))
#print(f'Hello, {planet_input.capitalize()} Nerd!')
#print(f'Hello, {} Nerd!'.format(capitalized_planet))

#This syntax may be a better choice
print(f'\nHello, {planet_input.capitalize()} Wizard! We have used "f" and I am a function put in curly braces')
print(f'Hello, {capitalized_planet} Nerd! We have used "f" and I am a variable put in curly braces')

#---------------------------------- Example 2 - Multiple Values to format in string -------------------------------
print("\n\nExample 2 - Multiple Values to format in string")
print("---------------------------------------------------")
a = 'Salt'
b = 'Sugar'

if a != b:
    print(f'a is {a} and b is {b}. {a} is not {b}')

print('a is {} and b is {}. Why compare {} and {}?'.format(a,b,b,a))

#------------------------------------------------------------------------------------------------------------------
