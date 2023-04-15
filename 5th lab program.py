'''Tuples in Python are ordered , unchangable and allow duplicates
to append elements in a tuple their is one problem we can't change the tuple if created means we can't add or remove
element in tuple if it is created'''
#tuple1.append(23) #Error777() '''
l =[]
a = int(input("Enter how many elements you want"))
for i in range(0,a):
    l.append(int(input()))
tuple2 = tuple(l)
print(tuple2)
print(type(tuple2))
h = int(input("Enter an element  : "))
a = tuple2.index(h)
print("index of element  =  ",a)
a = tuple2.count(h)
print("Occurance of element  =  ",a)