# def sumTwo(a , b ):
#     sum = a + b;
#     return sum
# a = int(input("Enter  1st number  :  "))
# b = int(input("Enter 2nd number  :  "))
# sum  = sumTwo(a,b)
# print("Sum of two numebrs  =   ",sum)
#
# def fact(a):
#     fac = 1
#     for i in range(1,a+1):
#         fac = fac * i
#     return  fac
# a = int(input("Enter a number   :   "))
# fac = fact(a)
# print("Factorial of a give number   =  ",fac)
#
# def swap(a,b):
#     a , b = b , a
#     print("Numbers after swapping")
#     print(a,b)
# a = int(input("Enter first number  :  "))
# b = int(input("Enter second number  :  "))
# swap(a,b)
# def reverseNum(a):
#     ans = 0
#     while(a>0):
#         ans= ans * 10 + (a%10)
#         a = int(a / 10)
#     return ans
# a = int(input("Enter a number :  "))
# ans = reverseNum(a)
# print(ans)
x= lambda a: a/10
print(x(10))