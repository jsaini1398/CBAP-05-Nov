# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:25:33 2020

@author: vikas
"""

#Numpy

import numpy as np

np.random.randint(100, 1000)

np.random.randint(1000)

# Scalar
x0 = np.random.randint(10, 100, size = 10)

type(x0)

x0
print (list(x0))

x0.size

x0.shape


# 2-Dim
x0
x1 = np.random.randint(10,100, size = (3,4))
x1


print (x1.shape)
print (x1.size)


# 3-Dim

x3 = np.random.randint(10, 100, size =(2,3,4))

x3

print(x3.size)
print (x3.shape)


x0

x0[1:4]

x0[:-2]

x0[-2]



import numpy as np
x2 = np.random.randint(10,20, size=(5,5))

x2

x2[0][0]

x2[0][4]

x2[0,2:5]

x2
x2[1:4,0:2]
x2.shape

x2

x2[1:3,1:3]


x2[2:4 ,2:4 ]

x2



import numpy as np

x2 = np.random.randint(10, 20, size=(5,5))
x2.shape

x2                       
x2[2][2]
x2[4][3]

x2

#2-Dim
x2[1]

x2[0,0]
x2[0,1]  #1st row, 2nd col
x2[0,2]
x2[0,3]

x2[1,0]
x2[1,1]  #1st row, 2nd col
x2[1,2]
x2[1,3]

x2

x2[0:,0:]  #all

x2[:,:]
x2  #full array


x2[0:2,0:2]  #1st row

x2
x2[4,3]


x2[:1, 2:4]

x2[:,1:2]  #1st col

x2[:, :1]


x2[:2, :3] #first 2 rows, first 3 columns

x2

x2[1,-2:]

x2

x2[1,-2]
x2



#alternate items
x2[::, ::] #all

x2[::2,::2]


x2[::2, ::] #alternative rows
x2[::, ::2] #alternative cols


x2
#3-Dim
x3  #all
x3[::] #all
x3[1::] #2nd matrix onwards
x3[::2]  #alternative matrix
x3[1:2:] #2nd matrix
x3[0,0,0]  #first cell
x3[2,3,4]  #last cell of array
x3[0]  #first matrix
x3[0,1]  #first matrix, 2nd row
x3[1,2] #2nd matrix, 3rd row
x3






#Index with Numpy



import numpy as np

array = np.arange(20)
print (array)

array1 = np.arange(10, 20)
print (array1)

array2 = np.arange(10,30,2)
print (array2)

type(array2)



array2.shape
array2

reshape_array = array2.reshape(3,5) #ValueError: cannot reshape array of size 10 into shape (3,5)


reshape_array = array2.reshape(5,2)
reshape_array

reshape_array = array2.reshape(2,5)
reshape_array
reshape_array.shape


array3 = reshape_array.reshape(10)
array3.shape

rs = reshape_array.shape
rs

array4 = reshape_array.reshape(rs[0]*rs[1])

array4.shape

array4

arr5 = array4  + 1
arr5


a = np.zeros((2,4))
a


a = np.zeros((2,4), dtype = int)
a


b= np.ones((2,4), dtype = int)
b


c = a+b
c

d = c+b
d

e = d*c
e


f = np.empty((2,3), dtype=int)
f


g = np.eye(3,3)
g



h = np.linspace(0,10, num = 5)
h


array6 = np.array([10, 30, 20, 50])
array6


array7 = np.array([[1,2,3],[5,6,7]])

array7


l1 = [[1,2,3],[5,6,7]]
array8 = np.array(l1)
array8




x=np.random.randint(60,100, size=100)
x

min(x)
max(x)

max(x) - min(x)

np.mean(x)
np.median(x)
np.std(x)
np.var(x)

ls1 = np.linspace(10, 15, 9)
ls1

ls1.round(1)

np.floor(ls1)
np.ceil(ls1)
np.trunc(ls1)




np.floor([1.2, 1.6])
np.ceil([1.2, 1.6])
np.trunc([1.2, 1.6])

np.round([1.2, 1.6])


np.trunc([-1.2, -1.6])
np.floor([-1.2, -1.6])

np.pi


fname = np.char.array(['Vikas', 'Kounal'])
fname

lname =  np.char.array(['Khullar', 'Gupta'])
lname

name= fname + lname
name


x4= np.array([1,2,3,4,5])
x4.size

x4a = np.concatenate([x4, np.zeros(5), np.ones(5)])
x4a


x5 = np.random.randint(0, 9, size=(2,3))
x5
x6 = np.random.randint(0, 9, size=(2,3))
x6
x7 = np.concatenate([x5,x6])
x7
x7a = np.concatenate([x5,x6], axis=0)
x7a
x8 = np.concatenate([x5,x6], axis= 1)
x8

# for Concatenation Dimentions must match exactly
x5a = np.random.randint(0, 9, size=(2,3))
x5a
x6a = np.random.randint(0, 9, size=(3,2))
x6a


'''
Dot product of two arrays. Specifically,
If both a and b are 1-D arrays, it is inner product of vectors (without complex conjugation).
If both a and b are 2-D arrays, it is matrix multiplication, but using matmul or a @ b is preferred.
If either a or b is 0-D (scalar), it is equivalent to multiply and using numpy.multiply(a, b) or a * b is preferred.
If a is an N-D array and b is a 1-D array, it is a sum product over the last axis of a and b.
If a is an N-D array and b is an M-D array (where M>=2), it is a sum product over the last axis of a and the second-to-last axis of b:
'''  
    
    
    
np.matmul(x5a,x6a)
np.dot(x5a,x6a)


#vertical and Horizontal Stack
x=np.arange(6).reshape(2,3)
x
y=np.arange(10,16).reshape(2,3)
y

np.vstack([x,y])
np.hstack([x,y])


x=np.arange(16).reshape(4,4)
x

np.split(x,2)

np.split(x,2, axis =0)

np.split(x,2, axis =1)


print(x)

x.min()
x.min(axis=0)
x.min(axis=1)


x.max()
x.max(axis=0)
x.max(axis=1)


x.max()
x.max(axis=0)
x.max(axis=1)

x.sum()
x.sum(axis=0)
x.sum(axis=1)

x.mean()
x.mean(axis=0)
x.mean(axis=1)


x=np.random.randint(30,50, size=200000)

x=np.array([30,49,50,60, 49])
x
np.equal(x, 49)
np.greater(x,48 )
np.less(x,48)
np.greater_equal(x,49)
np.less_equal(x,49)

np.sum(x>49)


x=np.arange(16).reshape(4,4)
x

np.sum(x>10, axis=0)

np.sum(x>10, axis=1)


np.any(x>14)

np.all(x>10)
np.all(x>=0)

x
np.sum((x>3) & (x<10))


x=np.random.randint(30,50, size=10)
x
x.sort()
x

np.sort(x)[::-1]


x=np.arange(16).reshape(4,4)
x
x.T



import matplotlib

from matplotlib import pyplot as plt
import numpy as np

n_arr= np.random.normal(50,20,100)
n_arr

n_arr.mean()
n_arr.std()
n_arr.size
n_arr.max()
n_arr.min()

plt.hist(n_arr)




































