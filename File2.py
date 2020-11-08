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


lc = [3,2,6,5,8]
lc.sort()
lc

lc.sort(reverse=True)
lc

lc = [3,2,6,5,8]
lc.reverse()
lc

max(lc)
min(lc)



a = math.sqrt(1030)
math.floor(a)


g= str(" this is sachin's laptop")
print(g)

import math
a = 10.4
b =math.ceil(a)
c =math.floor(a)
type(b)
type(c)
print (b, c)

print (math.cos(0))

print (math.sin(0))
print (math.exp(3))
print (math.factorial(10))
print (math.gcd(10, 200))
print (math.log(10, 2))
print (math.pow(10, 5))
print (math.pi)
print (math.sqrt(10000))
print (math.tan(45))




#Tuple
# Hetro, immutable or not changeble, indexed

t1 = (20,30, 40, 50)
type(t1)
#Hetro

t1 = (20, "vikas", True, 333.44)


#indexed
print (t1[0])

#Not Changeble
t1[0] =20 #TypeError: 'tuple' object does not support item assignment




for i in t1:
    print (i)
    
    
t2 = ("Vikas", "Raman", "Amit")

t2[1]

for i in t2:
    print (i)


"Amit" in t2
"Khullar" in t2


if ("Amit" in t2):
    print ("Yes")

if ("Khullar" in t2):
    print ("Yes")
   

t2
t2.append(220)    #AttributeError: 'tuple' object has no attribute 'append'
t2.remove() #AttributeError: 'tuple' object has no attribute 'remove'

len(t2)

t3 = (20, 20, 30, 40, 20)
t3.count(30)
t3

#unordered
t3 = (10, 20, 50, 40, 30)
print(t3)


#Set
# Hetro, mutable, ordered, unindexed, {}

#Hetro
s1= {"Vikas", 20, 20.33, True}
s1
type(s1)

# No-Repet #Ordered Outcome
s1 = {3, 2, 1, 4, 1}

s1

#unindexed

s1[0] #TypeError: 'set' object is not subscriptable

for i in s1:
    print (i)


for i in s1:
    print (i, end = "-")


s1.add(5)
print (s1)

#No duplicate element allowed
s1.add(4)
print (s1)

s1.update([3,10])
print (s1)


s1.remove(5)
s1

s1.remove(7) # KeyError: 6

print (s1.discard(5))

s1
print (s1.remove(3))

s1
print (s1.pop())
s1
print (s1.pop())
s1

print (s1.pop(3)) #TypeError: pop() takes no arguments (1 given)


s1
s1.clear()

s1

del s1

s1 = {1,2,3,4,5,6}
s2 = {3,4,5,6,7,8}

s1.union(s2)

s1.intersection(s2)

s1.difference(s2)


teamA = {'India', 'Australia','Pakistan', 'England'}
teamB = {'Bangladesh', 'New Zealand', 'West Indies', 'India'}
teamA
teamB
#add Sri Lanka to TeamA
#create a teamC with all teams
#Perform all the set operations 
teamA.union(teamB)
teamA.intersection(teamB)
teamA.difference(teamB)


s4 = {'ab', 'abb', 'ac'}
s4

s5 = {1, 11,2 }
s5

s6 = {1, 11,'2', '$2' }
s6

s4 = {1.1, 1.11, '1', 1.4}
s4

s5 = {1, 1.3, 2.0, 0.5}
s5


# Dictionary

#Mutable, Unordered, no-index, key-value pair

#key value pair

# {Key:Value}


stud  = {'rollno':1, 'name': 'Vikas', 'Batch': 'CBAP', 'Joined': True}

print (stud)
print (type(stud))


# No rep in keys
stud1  = {'rollno':1, 'name': 'Vikas', 'name': 'vicky', 'Batch': 'CBAP', 'Joined': True}
stud1


# Not indexed
stud[1] # KeyError: 1


#Access using keys
stud['name']


car = {'brand':'Honda', 'model':'Jazz', 'year': 2020}

#Access
car['brand']

car['model']

car.get('brand')


#changeble or mutable

car['brand'] = 'Nissan'

print (car)


#list all keys

for i in car:
    print (i)

for i in car:
    print (car[i])
    
    
car.keys()

car.values()

car.items()

l_car = list(car.values())
l_car

l1_car = list(car.items())
l1_car


for i,j in l1_car:
    print (i, "  ", j)



'model1' in car.keys()

if ('model' in car.keys()):
    print ("Yes Existing")


car['color'] = 'Black'
car

car['color'] = 'White'
car


pop_ele = car.pop('color')
pop_ele

car

pop_ele = car.pop() #TypeError: pop expected at least 1 argument, got 0
pop_ele

pop_ele = car.pop(1) #TypeError: pop expected at least 1 argument, got 0
pop_ele


pop_ele = car.popitem()
print (pop_ele)

car


del car['model']
car

car.clear()
car

del car
car #NameError: name 'car' is not defined



l1 = [1,2,3,4]

l2 = l1

l1[2]=55

l1
l2


l3 = l1.copy()
l1[2] =77
l1
l3

student = {'rollno':[1,2,3,4], 'Name':['A','B','C','D']}
student

student['rollno'][0:3]

student['Name'][0:3]




car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

car['color']

car



import random
stud_raw = {'rollno':list(range(100)),'marks': list(range(1000,1100))}
stud_raw['marks']

import pandas as pd

df = pd.DataFrame(stud_raw)
df.to_csv("stud.csv")


#frozenset


# unmutable ot not changeble

b = {2,3,4}
type(b)

b.add(5)

fz1 = frozenset([1,2,3])
fz1
type(fz1)
fz1.add(10) #AttributeError: 'frozenset' object has no attribute 'add'



#Enumerate

l1 = ['eat', 'sleep', 'walk']

print (l1)

e1 = enumerate(l1)

print (e1)

print (list(e1))


e2 = enumerate(l1, 100)

print (e2)

print (list(e2))


for i in l1:
    print (i)


e2 = enumerate(l1, 100)

for i in e2:
    print (i)


l2 = list(range(100,200))
e3 = enumerate(l2)

count =0

for i in e3:
    if count ==  40:
        break
    print (i)
    count = count +1
    
for i in e3:
    print (i)


for i in e3:
    print (i)



l2 = list(range(5))
e3 = enumerate(l2)

e3.__next__()
e3.__next__()
e3.__next__()
e3.__next__()
e3.__next__()
e3.__next__() #StopIteration


#Zip

name = ["virat", 'Shikhar', 'Ravi', "Rahul"]
roll = [4,2,3,1]
marks = [40, 70, 50, 60]

zm1= zip (name, roll, marks)
print(zm1)

lzm1 = list(zm1)
print (lzm1)


zm2= zip (name, roll, marks)
print(zm2)

for i in zm2:
    print (i)

zm2= zip (name, roll, marks)
zm2.__next__()
zm2.__next__()
zm2.__next__()
zm2.__next__()
zm2.__next__() #StopIteration
