
###############################
print("Swapping values")
###############################

a, b = 5, 10
print (a, b)
a, b = b, a
print (a, b)

###############################
print("\nList conprehentions")
###############################

lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1] 
print(lst)

###############################
print("\ncreate single string from list items")
###############################

a = ["Python","is","the","Best"]
print(" ".join(a))

###############################
print("\nFind The Most Frequent Value In A List.")
###############################

a = [1,2,3,4,5,6,7,8,1,1,1]

print(max(set(a),key=a.count))

###############################
print("\nReverse a String")
###############################

a = "Hola como estas"
print(a[::-1])


###############################
print("\nReverse a List")
###############################

a = [1 ,2,3,4,5]
print(a[::-1])


###############################
print("\nTranspose 2d array")
###############################

a = [["a","b"],["c","d"],["e","f"]]
transposed = zip(*a)
print(list(transposed))


###############################
print("\nChained Comparison")
###############################

a = 6
print(4 < b < 7)
print(1 == b < 20)

###############################
print("\nChained function call")
###############################

def product(a,b):
	return a*b

def add(a,b):
	return a+b

b = True
print((product if b else add)(5, 10))

###############################
print("\nCopying List")
###############################

""" a fast way to make a shallow copy of a list """
a = [1,2,3,4,5]

b = a
b[0] = 10
""" both a and b will be [10,2,3,4,5] """

b = a[:]
b[0] = 10
""" only  b change to [10,2,3,4,5] """

"""copy list by typecasting method"""

print(list(a))

"""using the list.copy() method (python3 only)"""

print(a.copy())

"""copy nested list using copy.deepcopy"""
from copy import deepcopy

l = [[1,2],[3,4]]

l2 = deepcopy(l)
print(l2)


###############################
print("\nDictionary Get")
###############################

"""returning None or default value, when key is not in dict"""
d = {"a": 1, "b": 2}

print(d.get("c"))
print(d.get("c",3))

###############################
print("\nSort Dictionary by Value")
###############################

"""Sort a dictionary bt its values with the build'in function sort with key argument"""

d = {"apple": 1, "orange": 10, "tomato": -50}

print(sorted(d.items(),key=lambda x: x[1]))

###############################
print("\nFor else")
###############################
"""else gets called when for loop does not reach break statement """
a = [1,2,3,4,5]
for el in a:
	if el == 0:
		break
else:
	print('did not break out for loop')

###############################
print("\nConvert list to comma separated")
###############################

"""convert list to comma separated string"""
items = ["foo","bar","loo"]

print(",".join(items))

"""list of numbers to comma separated"""
numbers = [1,2,3,4,5]

print(", ".join(map(str,numbers)))

"""mix """

numbers = [1,"data",3,"NaN",5]

print(", ".join(map(str,numbers)))

###############################
print("\ndelete duplicates in list of lists")
###############################

k = []
k.sort()
list_mov = list(k for k,_ in itertools.groupby(k))

###############################
print("\nMerge dict’s")
###############################

""" merge dicts """
d1 = {'a': 1}
d2 = {'b': 2}

# python 3.5
print({**d1, **d2})

#other
print(dict(d1.items() | d2.items()))

#other
d1.update(d2)
print(d1)

###############################
print("\nMin and Max index in List")
###############################

""" find Index of Min/Max element"""

a = [1,2,3,3,4,5,6,7]

def minIndex(lst):
	return min(range(len(lst)), key=lst.__getitem__)

def maxIndex(lst):
	return max(range(len(lst)), key=lst.__getitem__)

print(minIndex(a))
print(maxIndex(a))

###############################
print("\nRemove duplicates from a list")
###############################

"""remove duplicates not preserve order"""
items = [1,2,2,2,5,122,44,44,10]

print(list(set(items)))

"""remove duplicates and keep the order"""
from collections import OrderedDict

items = ["foo","bar","bar","foo","apple","tomato","apple","tomato"]

print(list(OrderedDict.fromkeys(items).keys()))