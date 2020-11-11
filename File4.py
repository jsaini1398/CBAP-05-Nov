# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:50:43 2020

@author: vikas
"""

# Functions



a=10
b=20

print (a+b)
print (a-b)
print (a/b)
print (a*b)

#Other Statements

a=20
b=30

print (a+b)
print (a-b)
print (a/b)
print (a*b)

#Other Statements

a=40
b=20

print (a+b)
print (a-b)
print (a/b)
print (a*b)



'''
def Function_Name():
    Statements
    
    
Function_Name()
Function_Name()
Function_Name()
'''


def Mth():
    a = int (input("Enter a"))
    b = int(input("Enter b"))
    print (a+b)
    print (a-b)
    print (a/b)
    print (a*b)


Mth()

Mth()


def Mth1(a,b):
    print (a+b)
    print (a-b)
    print (a/b)
    print (a*b)
    
    
Mth1() #TypeError: Mth1() missing 2 required positional arguments: 'a' and 'b'

x=10
y=20
Mth1(x,y)



x=20
y=20
Mth1(x,y)

Mth1(30,50)


def printhello():
    print ("Hello")


printhello()


def printhello(name):
    print ("Hello ", name)

s1 = "Vikas"
printhello(s1)

printhello("Vicky")

printhello("Vinay")



l1 = [20, 30, 40, 50, 70, 90]
Total = 150

def perc(la):
    print ("PErcentage of ", la , "  -> ",(20/Total) * 100)


for la in l1:
    perc(la)



"""Define a function reverse() that computes the reversal 
of a string. For example, reverse("I am testing") should 
return the string "gnitset ma I"."""


def reverse(st):
    print ("Inside " ,st[::-1])
    return (st[::-1])

st2 = reverse("I am testing")
print ("Outside " , st2)

print ("Outside " ,reverse("Vikas"))





def Mth2(a,b):
    return (a+b, a-b, a/b, a*b)
    
u = Mth2(10,20)

type(u)

u,v,x,w= Mth2(10,20)

type(u)


print (u)




def detail(name, rno,  email = "None"):
    print(name, rno,  email)


detail('vikas', 112, 'vikas.khullar@gmail.com')

detail('vikas', 112)

detail('vikas', 'vikas.khullar@gmail.com', 112)

detail(name= 'vikas', email = 'vikas.khullar@gmail.com', rno= 112)







































