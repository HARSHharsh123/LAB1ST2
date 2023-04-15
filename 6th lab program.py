dict1 = {
    'Harsh' : 1,
    'Aakash':2,
    'Ashish':3,
    'Adesh':4,
    'Sahitya':5,
    'Colour': ["Red","blue","green"]

}
print(dict1)
#accessing particular value of key
print("Accessing particular value from key  :  ")
print(dict1['Harsh'])
print(dict1['Colour'])
print()
print("length of dictionary  :  ",len(dict1))
#to make a dictionary using dict() constructor
dict2 = dict(name = "harsh" ,age = 18 , country = "India")
print(dict2)
key = input("Enter key to get particular value  :  ")
value = dict1.get(key)
print(value)
#to print list of all keys
x = dict1.keys()
print("List of all keys  =  ",x)
#changing the value of key
dict1['Adesh'] = 29
print("After chaning the value of key we get : ",dict1)
#priing list of all values
x = dict1.values()
print("List of all values  =  " ,x )