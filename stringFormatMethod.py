#use of the format method on strings

#------------------------------------------ Example 1 - Use of format method --------------------------------------------------------------------------
print("Example 1 - Use of format method")
print("--------------------------------")
planet_input = input("Hi there! Which planet are you from?: ")
capitalized_planet = planet_input.capitalize()

#format method puts the argument it receives inside the curly braces '{}
print('\nHello, {} Geek! We have used "format" and I am a FUNCTION put in it'.format(planet_input.capitalize()))
print('Hello, {} Wizard! We have used "format" and I am a VARIABLE put in it'.format(capitalized_planet))
#print(f'Hello, {planet_input.capitalize()} Nerd!')
#print(f'Hello, {} Nerd!'.format(capitalized_planet))

#This syntax may be a better choice
print(f'\nHello, {planet_input.capitalize()} Intelligent Agent! We have used "f" and I am a function put in curly braces')
print(f'Hello, {capitalized_planet} Nerd! We have used "f" and I am a variable put in curly braces')

#---------------------------------- Example 2 - Multiple Values to format in string -------------------------------------------------------------------
input("\nHit enter to continue...")
print("\n\nExample 2 - Multiple Values to format in string")
print("---------------------------------------------------")
a = 'Salt'
b = 'Sugar'

print(f"{a} & {b} and variable values inserted in string with format method")
if a != b:
    print(f'a is {a} and b is {b}. {a} is not {b}')

print('a is {} and b is {}. Why compare {} and {}?'.format(a,b,b,a))


#------------------------------------------------------------------------------------------------------------------------------------------------------
input("\nHit enter to continue...")
print("\n\nExample 3 - Format aguments order manupulation")
print("--------------------------------------------------")

print('Order of whole numbers will be messed up if you mess up number names order in curly braces {3},{1},{0},{2}?'.format('Zero','One','Two','Three'))
print('Order of whole numbers will be messed up if you mess up format method arguments {0},{1},{2},{3}?'.format('Zero','Three','One','Two'))
print('Order format argument correspondingly to number names in curly braces and get it right --> {3},{1},{0},{2}?'.format('Two','One','Three','Zero'))

#------------------------------------------------------------------------------------------------------------------------------------------------------
input("\nHit enter to continue...")
print("\n\nExample 4 - Spacing and Padding with 0s")
print("--------------------------------------------------")

me = 'Jane'
him = 'Abraham'
print('Give me (12-me) spaces on my right "{me:<12}", and give him (7-him) spaces on his left "{him:>7}"')
print(f'Give me (12-me) spaces on my right "{me:<12}", and give him (7-him) spaces on his left "{him:>07}"')
print(f'Give me (12-me) spaces on my right "{me:<012}"', f'and give him (10-him) spaces on his left "{him:>010}"')
#------------------------------------------------------------------------------------------------------------------------------------------------------
