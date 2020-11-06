# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:08:59 2020

@author: vikas
"""

#List, Tuple, Set, Dictionary, Frozenset

# Hetrogeneous, Mutable, Ordered, Indexed

#List   [], 

l1 = []
type(l1)

l1 = [10, 20, 30, 40]
print (l1)
print (type(l1))

# Hetrogeneous
l2 = [20, 'Vikas', 30.22, True ]
print (l2)

#Indexed
print (l2[0])
print (l2[1])
print (l2[2])
print (l2[3])
print (l2[4])

print (l2[0:2])
print (l2[1:3])

print (l2[1:])
print (l2[:3])

len(l2)



a = range(10)
print (a)
la = list(a)
print (la)


b = range(10,20)
print (b)
lb = list(b)
print (lb)


c = range(10, 30, 2)
print (c)
lc = list(c)
print (lc)


lb[::2]
lb[2::3]

lb[-2]
lb[:-3]
lb[4:-2]
lb[-4:-2]
lb
lb[::-1]
lb[::-2]

lbr = lb[::-1]
lbr


# Mutable or Changeble
print (lb)

lb[2] = 33
print(lb)

lb[6] = 55
print (lb)

lb[10]= 77 # IndexError: list assignment index out of range

lb.append(77)
print (lb)

lb.append(107)
print (lb)

lb_pop = lb.pop()
print (lb_pop)
print (lb)


lb.append(107, 108,109) # Error

lb_pop = lb.pop(4)
print (lb)

print (lb_pop)


lb_pop = lb.pop(3)
print (lb)
print (lb_pop)

lb
lb_i = lb.index(16)
lb.pop(lb_i)
lb

lb.append(15)
lb
lb_i = lb.index(15)
lb_i
lb.pop(lb_i)
lb


print(lb)

for i in lb:
    print (i)



import math

a = 10.4
math.ceil(a)
math.floor(a)




