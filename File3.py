# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:47:14 2020

@author: vikas
"""

# Conditions

'''
if(condition)
{
subcode 
}

if (Condition):
    subcode

'''

a = 10
b = 20
a = b # Assignment Opertator Wrong for conditional statement


a = 10
b = 20
a == b
a<10
a>b
a<=10
a>=b
a!=b


x=2

if(x==2):
    print ("Right")


if(x!=2):
    print ("Right")


x = 20
y = 30


if (x>y):
    print ("x is greater")
else:
    print ("y is greater")


if (False):
    print ("x is greater")


Marks = int(input("Enter Marks -> "))
type(Marks)

if(Marks > 80):
    print ("A")
elif(Marks>70 and Marks<=80):
    print ("B")
elif(Marks>60 and Marks<=70):
    print ("C")
elif(Marks>50 and Marks<=60):
    print ("D")
else:
    print ("F")


# Ladder if else

Marks = int(input("Enter Marks -> "))
type(Marks)
if (Marks>80):
    print ("A")
else:
    if(Marks>70 and Marks<=80):
        print ("B")
    else:
        if(Marks>60 and Marks<=70):
            print ("C")
        else:
            if(Marks>50 and Marks<=60):
                print ("D")
            else:
                print ("F")


x=7; y=5; z=6

if (x > y and y < z):
    print("Both conditions are True")



x=3; y=5; z=6

if (x > y or y < z):
    print("Both conditions are True")
    
    
L1 = ['abc', 'def', 'efg']    

if ('deff' in L1):
    print("Right")
else:
    print ("wrong")


s1= 'def'
s2 = 'def'


if (s1 == s2):
    print ('Right')
else:
    print ('Wrong')



# Iterative Statements

teamA = ['India', 'Aus', 'Pak', 'WI']

teamA[0]
teamA[1]
teamA[2]
teamA[3]

'''
Syntax

for [Simple Variable] in [Iterative Variable]:
    Proceeding Statements

'''

count = 0
print (count)

for tm in teamA:
    count =count +1
    print (count," " , tm)

count = 100
print (count)


LR = [0,1,2,3]

for i in LR:
    print (i)


for i in list(range(len(teamA))):
    print ("At Index ", i, ", Team is ", teamA[i])



LR1 = list(range(100, 110))
LR1
for i in range(len(LR1)):
    print ("At Index ", i, ", Team is ", LR1[i])






for i in range(10):
    print (i)
    
    
# Table of 2

for i in range(1,11):
    print ("2 * ", i, " = ", 2*i)
    
    
# Table of 10 Number Table


for i in range(1,11):
    for j in range(1,11):
        print (i, " * ", j, " = ", i*j)


RL  = [4,3,7,8,5,6]
RL1 = [4,3,7,8,6]

for i in RL:
    if (i == 5):
        print ("5 is available")
    

for i in RL1:
    if (i == 5):
        print ("5 is available")
    



# Break, Continue, Pass

RL  = [4,3,5,9,6]



for i in RL:
    if (i == 5):
        print ("Element Searched")
    print (i)
print ("Ended")


for i in RL:
    if (i == 5):
        print ("Element Searched")
        break
    print (i)
print ("Ended")


for i in RL:
    if (i == 5):
        print ("Element Searched")
        continue
    print (i)
print ("Ended")




#Searching

flg=0

for i in RL:
    if (i == 50):
        print ("Element Searched")
        flg=1
        break
    print (i)

if(flg==0):
    print ("Element Not Searched")
    

print ("Ended")




for x in range(20, 50, 3):
    print (x)



#While Loop

'''

while (condition):
    statement

'''



cnt =0

while (cnt < 10):
    print ("vikas")
    cnt = cnt + 1



flg=0
while(flg==0):
    key = input("Enter A Key -> ")
    if (key == "Z"):
        flg=1



while(True):
    key = input("Enter A Key -> ")
    if (key == "Z"):
        break



print("i =",1)
print("i =",2)
print("i =",3)
print("i =",4)
print("i =",5)
print("i =",6)
print("i =",7)
print("i =",8)
print("i =",9)




cnt = 1
while (cnt<=9):
    print("Count =",cnt)
    cnt =cnt+1



i=1
j=1S


while (i<=10):
    while(j<=10):
        print (i, " * ", j, " = ", i*j)
        j = j+1
    i = i +1    
    j = 1






































































































































