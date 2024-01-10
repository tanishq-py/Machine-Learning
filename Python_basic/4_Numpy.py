#numpy

import numpy as np

my_lst=[1,2,3,4,5]
arr=np.array(my_lst) #[1 2 3 4 5]

# Multinested array
my_lst1=[1,2,3,4,5]
my_lst2=[2,3,4,5,6]
my_lst3=[9,7,6,8,9]
arr1=np.array([my_lst1,my_lst2,my_lst3])

# output - array([[1, 2, 3, 4, 5],
#        [2, 3, 4, 5, 6],
#        [9, 7, 6, 8, 9]])

## check the shape of the array
arr1.shape #(3,5)


## Accessing the array elements 
arr   #array([1, 2, 3, 4, 5])
arr[3] #4

### Some conditions very useful in Exploratory Data Analysis 
val=2
arr[arr<3] #array([1, 2])

arr[3:]=100 #array([  1,   2,   3, 100, 100])

# Create arrays and reshape
np.arange(0,10).reshape(5,2)  
# output - array([[0, 1],
#        [2, 3],
#        [4, 5],
#        [6, 7],
#        [8, 9]])

## random distribution
np.random.rand(3,3)
#output array([[0.80892282, 0.71540909, 0.61908994],
       #      [0.47289906, 0.81495189, 0.37922198],
       #      [0.98095096, 0.17323863, 0.6673249 ]])















