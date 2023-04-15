#applications of lambda function using filter , reduce and map function ;;;;;
import functools
# lst1 = []
# lst2 = []
# a = int(input("Enter the size of first list  :  "))
# d = int(input("Enter the size of second list  :  "))
# for i in range(0,a):
#     ele = int(input())
#     lst1.append(ele)
# for i in range(0,d):
#     ele = int(input())
#     lst2.append(ele)
# lst_even = list(filter(lambda x : (x%2)==0 , lst1))
# print(lst_even)
# #now we do double using map function
# lst_double = list(map(lambda x : x*2 , lst1))
# print(lst_double)
# #now we do sum of two lists using map fucntion
# lst_sum = list(map(lambda  x,y : x+y,lst1,lst2 ))
# print(lst_sum)
lst1 = [10,20,30,40]
print(functools.reduce(lambda a,b: a+b, lst1))
#not we do reduce function