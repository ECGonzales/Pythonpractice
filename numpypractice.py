# https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
# My worked through notes

import numpy as np
from numpy import pi

a = np.arange(15).reshape(3,5)
print a             #If want to run in a code must use print statement.
print a.shape
print a.ndim
a.dtype.name        #If running in command line you can run as so
a.itemsize
a.size
type(a)
b = np.array([1,2,3]) # Need to have [] in parenthesis
b = np.array([(1,2,3,),(4,5,6,),(7,8,9)]) # sequence of sequences goes to a 3D array
c= np.array([ [1,2], [3,4] ], dtype=complex)
# to create an array full of zeroes or one full of ones
np.zeros( (3,4) )
np.ones( (2,3,4), dtype=np.int16 )
np.empty((2,3))     # creates an array of random values dtype is float64
np.arange(10,30,5)  # Creates an array from 10 to 25 in increments of 5

#np.arange is not the best to use with floating point numbers. Better to use linepace, so you know how many elements it outputs
np.linspace(0, 2, 9)  #Gives nine numbers from 0 to 2
x = linspace(0, 2*pi, 100)
f = np.sin(x)

# Create an array of numbers from 0 to 11 arranged such that there are 4 rows and 3 columns
b = np.arange(12).reshape(4,3) #2D array
'''print b
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''

#Create an array of numbers from 0 to 23 arranged such that there are 2 2D arrays of 3 rows and 4 columns
b = np.arange(24).reshape(2,3,4) #3D  array
'''print b
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
'''

# To print an entire array that is typically too large use command
np.set_printptions(threshold='nan')
#deafult is thereshold = 1000

#Arthemtic on arrays
b = np.arrange(4) #array([0, 1, 2, 3])
b**2              #array([0, 1, 4, 9])  squares each element
b*2               #array([0, 2, 4, 6]) doubles each element
a= np.array([20,30,40,50])
a < 35            # See if any element in the array is less than 35 answer is boolean
# To multiply arrays must use .dot() or np.dot(A,B)
A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
A.dot(B)
np.dot(A,B)

# When performing += or *= operations on an arrray the array is modified
a = np.ones((2,3), dtype=int)
b = np.random.random((2, 3))
a *=3
a
b += a # This converts a into a float, which is apparently doable
b
a+= b  # This will give an error "TypeError: Cannot cast ufunc add output from dtype('float64') to dtype('int64')
       # with casting rule 'same_kind'". This tries to convert b into an interger type

# To apply an operation to a specific axis of an array
b = np.arange(12).reshape(3,4)
print b
b.sum(axis = 0 )  # Sum of each column (axis = 0 column)
b.min(axis = 1)  # Finds minimum of each row (axis = 1 row)
b.cumsum(axis =1 )  # Sum row-wise as you go for each array element

# Universal functions operate element wise to entire array. EX: np.ex(), np.sqrt(), np.add()

# Slicing 1D arrays
a[:6:2] = -1000   # Starting with the first element, replace every other one with -1000 up to the 7th element.
a[ : :-1]  # Reverse the order of the array

# Multidimensional arrays
def f(x,y):
    return 10*x+y
b = np.fromfunction(f,(5,4),dtype=int) #fromfunction(function,shape,dtype-optional)
'''print b
[[ 0  1  2  3]          Prints a 5x4 matrix where to get elements use the function for each cord of matirx i.e
 [10 11 12 13]          first element is x,y = (0,0) => 0 from func. element (1,0) is then 10*1+0 = 10
 [20 21 22 23]
 [30 31 32 33]
 [40 41 42 43]]'''
b[2,3]  #picks out the element in the third row fourth column
b[0:5,1]  # Select entire second column or could do b[ : ,1]
# If you don't give the same number of indices as axis numpy assumes it is a complete slice.
b[-1]  # this gives the entire last row equivalent to b[-1, : ] or b[4, : ]

c = np.array([[[0,1,2],
              [10,11,12]],
             [[100,101,102],
              [110,111,112]]])
c.shape  # Tells you the shape of your array
c[1,...]  # Gives me the second row for all of the 2D arrays I have.
c[0,0,1]  # c[array,row,column]
c[...,2]  # Gives the last column for all 2D arrays I have

for row in b:
    print row

if __name__ == '__main__':
    for element in b.flat:  #Allows you to perform element wise operations in for loop.
        print element

# When you change the shape of the array if you want to keep using the reformatted array, rename the array since it
# really stays in its original shape.
a = np.floor(10*np.random.random((3,4)))  # Floor gives you an interger towards the lowest number i.e. if a =[-1.7,-1.5]
a.ravel()                                   # floor(a)= [-2.,-2.]
b= a.ravel()  # Turns array into one row
a.shape()
b.shape()
