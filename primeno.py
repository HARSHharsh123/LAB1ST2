a = int(input("Enter a number  :  "))
all = a==0 or a==1
if all:
    print(a," not a prime number")
else:
    for i in range(2,a):
        if(a%i==0):
            print(a , "is not a prime number")
            break
    else:
        print(a , "is a prime number")