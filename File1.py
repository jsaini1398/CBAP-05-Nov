# Welcome to CBAP

'''
Welcome to CBAP
Welcome to CBAP
Welcome to CBAP
'''

# F5 to run full file
# F9 to run selected line of code


print?

print ('Welcome to CBAP')
print ('Welcome','to CBAP')
print ('Welcome','to CBAP', sep =',')


print ('Welcome to CBAP', end='******')
print ('Welcome','to CBAP', end='*****')
print ('Welcome','to CBAP', sep =',', end='    ')

help(print)

help(numpy)

import numpy

help(numpy)

!pip install numpy

import numpy
numpy.__version__


!pip install --upgrade pip

!conda list

!conda search scipy



#Data Type
#integer int
#floating float
#string combination of charachters
#boolean True/False   1/0


a = input("Enter your name - > ")
print (a)

b= 'Khullar'
print(b)

print ()

print(1)

type(a)
type(b)


a = 10
b = 20

type (a)
type (b)


a = 10.4
b = 100.333

type(a)
type(b)

a = True
b = False

type(a)
type(b)


print (a)


print("Khullar's git")

a=10
b=20

print ("The value of a is {0} and b is {1}".format(a,b))

country = input("Enter your country name")

print (country)

print (f"I live in {country} which is very energetic country")

print ("I live in ", country , "which is very energetic country")



# Demonstrate int() Casting Function

a = 10.5
type(a)

float_to_int = int(a)

print (float_to_int)
print (a)

type(float_to_int)

b= '1'
type(b)

str_to_int = int(b)
print (str_to_int)

type(str_to_int)


# Demonstrate float() Casting Function

a = 10

int_to_float = float(a)
print (int_to_float)
type(int_to_float)

b ='10.55'
str_to_float = float(b)
print (str_to_float)
type(str_to_float)


# Demonstrate str() Casting Function

a = 10
int_str  = str(a)
print (int_str)
type(int_str)


b = 10.55
float_str  = str(b)
print (float_str)
type(float_str)


# Demonstrate chr() Casting Function

ascii_to_char = chr(30)
print(ascii_to_char)



#Operators

x = 20

print(x+1)
print(x)

print (x-1)
print (x*2)


print (x ** 2)

print (x/2)

print (x%2)
print (x%3)

print (x+1, x-1, x*2, x**2, x%2)


x = 20
x = x + 1
print(x)

x += 1
print (x)

x *=2
print (x)


#Boolean
# True or False

t = True
f = False
print (t)
type(t)
print (f)
type(f)

'''
AND
a b y
0 0 0
0 1 0
1 0 0
1 1 1

OR
a b y
0 0 0
0 1 1
1 0 1
1 1 1

'''
a = True
b = False
print (a, b)

y = a and b
print (y)

a = True
b = True
print (a, b)

y = a and b
print (y)



a = True
b = False
print (a, b)

y = a or b
print (y)

a = True
b = True
print (a, b)

y = a or b
print (y)

a = False
b = False
print (a, b)

y = a or b
print (y)



'''
NOT

a y
0 1
1 0
'''

a= False
y = not a
print (y)

a=10
b=20
a+b
#Strings

Fname = 'Vikas'
Lname = "Khullar"

name = Fname + Lname
print (name)

name = Fname + " " + Lname
print (name)

len(name)
len(Fname)


fname = input("Enter a Name ->")
print (fname)

lname = input("Enter a Name ->")
print (lname)

name = fname+lname


name = input("FName ->") + input("LName ->")
print(name)

name = input("Enter a Name ->")
print (name)

name = name.capitalize()
name = name.upper()
print (name)
name = name.lower()
print (name)

print (name.rjust(10))
print (name.ljust(10))
print (name.center(10))

st =  "Hello"
print (st)

st = st.replace("ello", "ay")
print (st)


name = input("Enter Name - >")
print (name)

name = name.strip()
print (name)


name ="Vikas Khullar CBAP Instructor"
name = name.split(" ")
print (name)



















