def add(num1,num2) :
  return num1+num2

add(3,4)

def add_list(lst):
    sum1 =0
    for i in lst:
        print(i)
        sum1=sum1+int(i)
    return sum1

add_list([1,2,3,4,5,6])

#lambda function
#anonymous function - a function with no name

def add(a,b):
  return a+b
add(69,69)
  
add= lambda a,b:a+b  #only possible if one condition in function
add(12,14)

even= lambda a:a%2==0 
even(63283628732)

#list comprehension in python
lst = [1,2,3,4,5]
type(lst)


[i for i in lst]  #[1,2,3,4,5]

lst2= [2,4,3,5]
[i for i in lst2  if i%2==0]  #[2,4]

#map function
def even_or_odd(num):
  if num%2==0:
    return True
  else:
    return False

even_or_odd(34)

lst = [2,3,5,6,7,8]
list(map(even_or_odd, lst))  #[True, False, False, True, False, True]

function , lambda, map function, list comprehension

#filter functions
def even(num):
  if num%2==0:
    return True

lst = [12,3,4,5,6,7]
list(filter(even, lst))  #[12, 4, 6]


  
