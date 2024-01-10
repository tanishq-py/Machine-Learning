try:
    ##code block where exception can occur
    a=1
    b="s"
    c=a+b
except NameError as ex1:
    print("The user have not defined the variable")
except Exception as ex:
    print(ex)

#  a=b


### try else
try:
    ##code block where exception can occur
    a=int(input("Enter the number 1 "))
    b=int(input("Enter the number 2 "))
    c=a/b 
    d=a*b
    e=a+b
    
except NameError:
    print("The user have not defined the variable")
except ZeroDivisionError:
    print("Please provide number greater than 0")
except TypeError:
    print("Try to make the datatype similar")
except Exception as ex:
    print(ex)
else:
    print(c)
    print(d)
    print(e)


##try else finally

### try else
try:
    ##code block where exception can occur
    a=int(input("Enter the number 1 "))
    b=int(input("Enter the number 2 "))
    c=a/b
    
except NameError:
    print("The user have not defined the variable")
except ZeroDivisionError:
    print("Please provide number greater than 0")
except TypeError:
    print("Try to make the datatype similar")
except Exception as ex:
    print(ex)
else:
    print(c)
finally:
    print("The execution is done")


#Custom exception
class Error(Exception):
    pass

class dobException(Error):
    pass

class customgeneric(Error):
    pass

year=int(input("Enter the year of Birth "))
age=2023-year
try:
    if age<=30 & age>20:
        print("The age is valid. You can apply for the exams")
    else:
        raise dobException
except dobException:
    print("The age is not within the range. You cannot apply for the exams")
