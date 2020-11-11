# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:42:30 2020

@author: vikas
"""

#Random Numbers


import random as rd

l1 = [111,222,333,444,555]

print (rd.choice(l1))


st1 = ("abcdefg")
print (rd.choice(st1))


professions = ["scientist", "philosopher", "engineer", "priest"]
rd.choice(professions)

rd.choices(professions, k=10)




la = list(range(1000, 2000))
la

rd.choices(la, k =10)



d1 = {1 :100, 2: 300, 3:400}

rd.choices(list(d1.keys()), k=10)




l1 = [1,2,4,5,6]
print(rd.choices(l1, k=3))


import random
weight_set = {20, 35, 45, 65, 82}  #set

weight = random.choice(tuple(weight_set))
print ("Randomly item from Set is - ", weight)


#
import random
weight_dict = { "Kelly": 50,  "Red": 68,  "Jhon": 70,  "Emma" :40 }
key = random.choice(list(weight_dict))
print ("Random key value pair from dictonary is ", key, " - ", weight_dict[key])


from random import randrange
randrange(10, 20)

from random import randrange

random.seed(0)
randrange(10, 20)

randrange(10, 20)

randrange(10, 20)

randrange(10, 20)

print (random.randrange(100))
print (random.randrange(0, 100))
print (random.randrange(0, 100, 20))
print(random.randint(0,100))


l2= []

for i in range(100):
    l2.append(random.randrange(0, 100, 10))

l2


























