# #boolean var
type(True)
type(False)

# #boolean functions
my_str= "Tanishq223"
print(my_str.isalnum()) #check if all char are numbers
print(my_str.isalpha()) #check if all char in the string are alphabetic
print(my_str.isdigit()) #test if string contains digits
print(my_str.istitle()) #test if string contains title words
print(my_str.isupper()) #test if string contains upper case
print(my_str.islower()) #test if string contains lower case
print(my_str.isspace()) #test if string contains spaces
print(my_str.endswith('k')) #test if string endswith a d
print(my_str.startswith('K')) #test if string startswith H

# #boolean and logical operators
True and False #false
True or False  #true
True and True  #true
True or True   #true

#lists
type([]) #list

# .append() is used to add elements in the list
myList= [1,69,"micheal"]
myList.append("trevor")

#Indexing in List
myList[1:4]

# insert in a specific order
myList.insert(2,"jesse")

# Pop() Method
myList.pop()  #trevor
myList.pop(0)  #1

#count():Calculates total occurrence of given element of List
lst=[1,1,2,3,4,5]
lst.count(1)

#Min and Max
min(lst)
max(lst)
