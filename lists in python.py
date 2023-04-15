L = list()
print(L)
L = list("hello World")
print(L)
L = list(input("Enter a list"))
print("List entered = ",L)
print("Accessing individual element in List : ")
for i in L:
    print(i)
print(type(L))
#item assignement is supported in lists -> lists are mutuable
#list vs strings
#list are similar as strings but their are minute difference
#similarity -> list contain length() function , indexing and slicing , membership operators , concatinaion and replication operator
#comparison operator
#accessing individual element
# difference -> storage and mutuability
#Storage -> list har ek character ki index pr character na daal te hue vaha pr us character ka reference dalti hai......
#but string har ek character ki index pr single character dalta hai
#we can do modificiation through list indexing and list slicing
L1 = [1,2,3,"Harsh","Shukla",'is','my','name']
L1[3:5]=[7,8]
L1[5:7]=[1]
print(L1)
L1.append(12);
print(L1)
#updating a list
L1[3] = 123
print(L1)
#DELETING list using del function
#del L1[1:4]
#print(L1)
#del L1
#del L1[0:3]
#True COpy of list
color = ["red","Yellow","Green"]
b = color
print(b)
b[0]="White"
print(color) #change occur due to shallow copy
#here true/deep ko nhi bani hai list ki ye toh shallow copy hai means do variable names same address ko point kar rhe hai
#toh isse hoga ye ki agr me b se koi change karta hun list me toh voh color me bhee reflect honge but true copy ka mutlb hota
#hai ki agr me koi change karu toh voh sirif ussi list me reflect ho kisi dusri me nhi...........
#for deep copy
color = ["pink","purple","pista"]
b = list(color) #here true copy of list is created
print(b)
b[0] = "White"
print(color) #no change due to deep copy