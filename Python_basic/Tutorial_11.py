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


  
