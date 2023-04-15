#lists in python
#List are mutuable datatypes
'''Taking input in list and priting elements in list'''
#through append function
l=[]
d = []
a = int(input("Enter how many elements you want  ?? "))
for i in range(0,a):
    l.append(int(input()))
print("Printing elements in list")
for i in range(0,a):
    print(l[i])
#list functions
'''1. l.append(element to be inserted) -> it appends an element at the last position in the list
   2. l.clear() -> it clears all element in the list(whole list is cleared) 
   3. l.copy() -> returns the copy of the list
   4. l.count() -> returns the occurance of element specified in the list
   5. l.extend() -> add elements at the last
   6. l.index() -> return the index of first occurance of the element with value
   7. l.insert() -> insert an element at any postion
   8. l.pop() -> it removes the element at the specified position
   9. l.remove() -> it removes the element with specified value
   10.l.reverse() -> reverse all element of the list
   11.l.sort() -> sort all elements of list'''
#1. clear() function
l.clear()
print(l)
print("list cleared successfuly")
#2. copy() function
d = ["harsh",'d',12,1.23,'d',"harsh"]
x = d.copy()
print(x)
#3. count() function
x= d.count('d')
print(x)
#4. extend() function
h = [5,6,8]
d.extend(h)
print(d)
#5. index() function
g = d.index("harsh")
print(g)
#6. insert() function
d.insert(2,"Shukla")
print(d)
#7. pop() function
ele = d.pop(2)
print(ele)
#8.remove() function
d.remove('d')
print(d)
#9.reverse() function
d.reverse()
print(d)
#10. Sort() function
h = [3,2,1]
h.sort()
print(h)
#11. Sort() list in decreasing order
l1 = ['A','a','B','c']
l1.sort(reverse = True)
print(l1)
#copy construct
