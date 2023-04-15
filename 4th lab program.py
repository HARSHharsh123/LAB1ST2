#Creating list of integers
lst = []
d=[]
n = int(input("Enter how many elements you want  ???  "))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print(lst)
'''#Creating list of Strings
lst = []
n = int(input("Enter how many elements you want  ???  "))
for i in range(0,n):
    ele = input()
    lst.append(ele)
print(lst)
#Creating list of float numbers
lst = []
n = int(input("Enter how many elements you want  ???  "))
for i in range(0,n):
    ele = float(input())
    lst.append(ele)
print(lst)'''
'''#Creating list of integers , flaots
lst = []
n = int(input("Enter how many elements you want  ???  "))
for i in range(0,n):
    ele = eval(input())
    lst.append(ele)
print(lst)'''
#removing all list
#we use clear() function
d = lst.copy()
lst.clear()
print(lst)
#removing particular element from list
t = int(input("Enter which element you want to remove  ???  "))
d.remove(t)
print(d)
#removing element from index
i = int(input("Enter which location you want to remove element  ?? "))
d.pop(i)
print(d)

