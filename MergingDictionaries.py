#Two ways of merging dictionaries

print("Method1: merge dictionaries with update()")
dic1={1:20, 2:20}
print("dic1 is: ", dic1)
dic2={3:30, 4:40}
print("dic2 is: ", dic2)
dic3={5:50, 6:60}
print("dic3 is: ", dic3)

dic1.update(dic2)
print("dic1.update(dic2) is dic1 merged with dic2 is: ", dic1)
dic1.update(dic3)
print("dic1.update(dic3) is dic3 merged with modified dic1 is: ", dic1)

print("dic1 is now: ", dic1)

#merge dictionaries by making a list of them
print("\n")

print("Method2: merge by making a list of dictionaries")
dic4 = {'a':70, 'b':20}
print("dic4 is: ", dic4)
dic5 = {'c':30, 'd':40}
print("dic5 is: ", dic5)
dic6 = {'e':50, 'f':60}
print("dic6 is: ", dic6)
dic7 = {'g':20, 'h':20}
print("dic7 is: ", dic7)
dic8 = {'i':30, 'j':40}
print("dic8 is: ", dic8)
dic9 = {'k':50, 'l':60}
print("dic9 is: ", dic9)


list1 = []
list2 = []
merge_dict = {}

list1.extend(dic4.keys())
list1.extend(dic5.keys())
list1.extend(dic6.keys())
list1.extend(dic7.keys())
list1.extend(dic8.keys())
list1.extend(dic9.keys())

list2.extend(dic4.values())
list2.extend(dic5.values())
list2.extend(dic6.values())
list2.extend(dic7.values())
list2.extend(dic8.values())
list2.extend(dic9.values())

for x in range(0, len(list1)):
    merge_dict.update({list1[x]:list2[x]})
print(merge_dict)

'''
myDictList = [dic4, dic5, dic6, dic7, dic8, dic9]
print("Merged dic: ", myDictList)
print(type(myDictList))

dict(myDictList)
print(type(myDictList))
'''





