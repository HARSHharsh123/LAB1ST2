import math
a = 10
b=10
print(a is b)
a = oct(int(input()))
print(a,type(a))
text = "hello\
       world"
print(text)

print('''Helllo
        world''')
#Non Graphic Characters that are
text = 'hello student\'s \s'
print(text)
a = 2+3j
print(a , type(a))
a = bool({})
print(a, type(a))
#identity operatorv -> checks the addresss of the object means object id if object id of both variables are same
#then it returns True otherwise false
#== equality operator also works same as identity opertor except it checks the object means value in variable
# if value in both variables are same then it returns true otherwise false
# is and is not
a = "hello"
b = "hello"
print(a is b)
print(a==b)
'''Punctuators are used to organsize and indicate the rythm of statement , sentence , program'''
x=10
x = 'hl'
a=b=c=10
print(a,b,c)
a,b,c= 10,'a',True
print(a,b,c)
x,y=10,20
print(x,y)
x,y= y,x
print(x,y)
print("Hello","Shukla ji","kiya",sep='...')
b = 2+3j
print(b.real)
print(b.imag)
a = ("harsh",1,2,3,None,[1,2,'Harsh'],{'a':1,'b':2 , 'c':3},True, False , (1,2),22/7,2+4j)
print(a)
#mutuable -> changable or modifiable
# string , tuple , int , float , complex , None
a = 10
print(id(a))
a = 20
print(id(a))
'''if id of a in both cases is same then we can say that intger is mutuable otherwise it is immutuable because
 ab voh a voh a nhi rha ab voh kuch or ban chuka hai means both cases me a ki id change ho gai hai means hum 
 same memeory location me change nhi kar rhe dusri location me change ho rha hai '''
#immutable -> unchangable or non modifiable
#list , dict , set
l = [1,2,3,4,'Harsh']
print(l)
l[0] = 12
c = 6/2
print(c)
c = 6.0//2
print(c)
c = 6.0 + 2
print(c)
c = 2.0+3j + (90-40.0)
print(c)
print(c.real)
print(c.imag)
print(2>3<4)
#python evaluates this expression as (2>3) and (3<4)
#logical expression evaluation
print(6/2 or 3.0+2)
#type casting (explicit type conversion)
a = int(6.0) + 3
print(a)
#math library functions work for all number datatype except complex type
print(math.ceil(1.98))
print(math.ceil(-9.89))
print(math.sqrt(2))
print(math.fabs(-20))
print(math.floor(1.98))
print(math.floor(-9.89))
print(math.log(8,10))
print(math.log10(8))
print(math.pow(2,3))
print(math.sin(math.radians(90)))
print(math.cos(math.radians(0)))
print(math.tan(math.radians(0)))
print(math.fmod(-9.0 , 3.0)) #but fmod ka mainly hum istemaal karte hai for geting the more precision or it is mainly used
#for floating pointer numbers it also reflects the negative reaminder if exists
print(-9.0 % 3.0) # yaha negative remainder batayega hi nhi
print(7.4 % 3.3)
print(-8.3 % 6) #yaha galat ans a rha hai becuase negative floating point number hai isliye
print(math.fmod(-8.3 , 6)) #this answer is correct
#so as a result if number is a floating point number and contains negative value then we use fmod() function
print(math.fmod(18,-7))
#agr dono number integers hai or dono me positive sign hai toh hi modulus ka istemaal karna hai
#otherwise we use fmod function
print(-18%7)#aswer is wrong
print(math.factorial(5))
pass #empty statement jiska kaam hai do nothing
print(math.gcd(6,9))
#Control Statements ( if , else , if else if ladder , nested if)
#named conditions means
a = 5
b = 6
c = a
all = id(a) == id(c) and a<b>c #Named condition or storing condition
if all:
    print("Shi kiya hai")
else:
    print("Kitni galti karta hai")
sequence = [2,4,5,8,19]
for i in sequence:
    print(i)
for i in range(5):
    print(i)
for i in range(2,5):
    print(i)
for i in range(1,9,1):
    print(i)
for i in range(10,4): #it doesn't execute range is out of range
    print(i)
#range(stop) -> starts from 0 to stop - 1 with step 1
#range(start , stop) -> starts from particular value and end with a particular value with step 1
#range(start , stop , step) -> with mentioned step value
#more about loops
#loop else clause -> mutlb is else clause ki statements tab execute honge jab while or for loop pura execute ho jayga
#bina kisi problem ke but yaha agr hum break staement laga dete hai toh phir loop else clause will not execute
for i in range(1,5):
    if(i%8==0):
        break
    print(i)
#else clause without if beacuase it is not else statement it is loop else cluase
else:
    print("successfully printed numbers from 1 to 4")
for i in range(1,5):
    if(i%2==0):
        break
    print(i)
#else clause here it not execute because we do a break statement
else:
    print("successfully printed numbers from 1 to 4")
#concept of nested for loop
for i in range(1,5):
    for j in range(1,5):
        print("*",end = ' ')
#first phase completed