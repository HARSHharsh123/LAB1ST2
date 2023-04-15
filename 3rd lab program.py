#string concatination , replication , slicing
a1 = "Harsh "
a2 = "Shukla "
#concatiantion of strings

print("Concatination of two strings  =  ",a1+a2)
#Replication of strings

print("Replication of strings  =  ", a1*3)


'''error in concatination and replication of strings
print("Concatination of two strings  =  ",a1+2)ERROR IN THIS CASE
print("Replication of  strings  =  ",a1*a2)ERROR IN THIS CASE'''


#Slicing of strings
print(a1[1:3])
print(a1[:3])
print(a1[:])#no parameter concept
print(a1[::-1])#reverse string concept
print(a1[0:8])#outof bound concept
print(a1[8:6])#No OUTPUT
print(a1[1:2:2])
print(a1[-6:-1:1])#printing the original name by using negative indexing
print(a1[-9:-9])#no output(empty output)
print(a1[-5:3])
