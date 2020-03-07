#Use of 'is'
list_123 = [1, 2, 3]
list_321 = [3, 2, 1]
tuple_123 = (1, 2, 3)
tuple_321 = (3, 2, 1)

# == compares the value of both operands
if id(list_123[0]) == id(list_321[2]):
    print(f'ID of 1st element of list_123 is {id(list_123[0])} and is same as id of 3rd element of list_321 {id(list_321[2])}')
else:
    print('id of list_[1]23 {id(list_123[0]) is not same as id of list_32[1] {id(list_321[2])}')

print()
if id(list_123[0]) is id(list_321[2]):
    print(f'Object of 1st element of list_123 IS same as object of 3rd element of list_321')
else:
    print('Object of 1st element of list_[1]23 IS NOT same as Object of 3rd element of list_32[1]')

print()
print("id of tuple_[1]23 is: ", id(tuple_123[0]))
print("id of tuple_32[1] is: ", id(tuple_321[2]))

print()
# is checks if both operands refer to same object
print("object of list_123[0] is same as object of tuple_321[2]: ", id(list_123[0]) is id(tuple_321[2]))

print()
print("list_123 is a tuple: ", isinstance(list_123, tuple))
print("tuple_123 is a tuple: ", isinstance(tuple_123, tuple))
