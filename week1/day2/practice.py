# Practice lists, sets, tuples, dictionaries

#.................................... lists (mutable, ordered)....................................
#   add,remove,update
my_list=[1,2,3,4,5]
my_list.append(6)
my_list.remove(3)
print(type(my_list))
print("list after apppend 6 and remove 3:",my_list)

# pop func 
s = []
s.append('a') 
s.append('b')
print("list after pop:",s.pop())

# Iteration and Data Processing
#   1. Calculate the sum of all elements in a list
a = [1, 2, 3, 4, 5]
t = sum(a)
print("Total: ", t)

#  2. We split a sentence into words using split() func and convert each word to uppercase using a loop
s = "Subtle art of not giving a bug"
w = s.split()
for word in w:
    print(word.upper())

# 3. Create a list of squares of numbers from 0 to 9 using a loop
s = []
for i in range(10):
    s.append(i * i)
print("squares from 0 to 9:",s)



#.................................... tuples (immutable, ordered)................................
#   add,remove,update  (not possible)
p= (10, 20,30,40,50,60)
print(type(p))
print(p)

# 1. count the no A grade student in tuple
grade=('A','B','C','D','A','A','A','A','A')
print("count the no of A grade in tuple:",grade.count('A'))

# 2. find the index of a particular element in tuple
my_tuple = (10, 20, 30, 40, 20)
index = my_tuple.index(20)
print(index)

tup=(1,2,3,4)
print(tup.index(4)) 

#........................... dictionaries (mutable, unordered,don't allow dublicate key value)..........................
# Dictionaries store data in key:value pairs
my_dict={'name':'john','age':25,'city':'newyork'}
print(type(my_dict))
print("dictionary:",my_dict)

#changing name
my_dict["name"]="hammad"
print(my_dict)
print(my_dict['name'])

# add new key:value in dict 
my_dict['profession']='developer'
print("after adding new key value in dict:",my_dict)

# remove key:value from dict
del my_dict['age']
print("after removing age from dict:",my_dict)

# iterate through dict
for key, value in my_dict.items():
    print(f"{key}:{value}")

# 1. count frequency of each character in a string using a dictionary
s = "hello world"
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print("character frequency:",freq)

# 2. add multiple enteries using loop in dict
my_dict = {}

n = int(input("How many items you want to add? "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

print("Final dictionary:", my_dict)




#.................................... sets (mutable, unordered, don't allow dublicate)..........................
# sets store unique elements
my_set={1,2,3,4,5,5,5}
print(type(my_set))
print("set after removing dublicate 5:",my_set)