 # Defining string
str1= "hello"
str2= "world"
print(str1) # hello
print(str2) # world

#concatenation
str1= "Abhinay"
str2= "samrat"
result= str1+ " "+str2
print(result) # Abhinay samrat

#repetation 
str1= ("python!")
print("python!"*3) # python!python!python!    
str2= (" abhinaysamrat!!")
print("abhinaysamrat!!"*3) # abhinaysamrat!!abhinaysamrat!!abhinaysamrat!!       


#indexing string
str = ("python")
print(str[0]) # p
print()
print(str[-1]) # n

#slicing string
str = ("pythoniseasy")
print(str[0:3]) # pyt
print()
print(str[-1]) # y
print()
print(str[0:12]) # pythoniseasy
print()
print(str[:4]) # pyth
print()
print(str[2:]) # thoniseasy

#membership string
str = ("python","java","code")
print("python" in str ) # True
print()
print("java"not in str) # False
print()
print("code" in str) # True
print()
print("program"not in str) # True


# built-in string function
print("built in string function") # built in string function  
str = ("pythoniseasytolearn")
print("the length:",(len(str))) # the length: 19
print()
print("max value:",(max("pythoniseasytolearn"))) # max value: y
print()
print("min value:",(min("pythoniseasytolearn"))) # min value: a
print()
print("sorted :", (sorted("pythoniseasytolearn"))) # sorted : ['a', 'a', 'e', 'e', 'h', 'i', 'l', 'n', 'n', 'o', 'o', 'p', 'r', 's', 's', 't', 't', 'y', 'y']
print()
print("ordinal value:",(ord("h"))) # ordinal value: 104    
print()
print("unicode value:",chr(65)) # unicode value: A

#case conversion methods
print("case conversion method") # case conversion method    
PYTHONISEASYTOLEARN       

pythontolearn

Python

Python And Java

aBhInAY
str1 = ("pythoniseasytolearn")
print(str1.upper()) # PYTHONISEASYTOLEARN       

print()
str2 = ("PYTHONTOLEARN")
print(str2.lower()) # pythontolearn
print()
print("python".capitalize()) # Python
print()
print("python and java".title()) # Python And Java
print()
print("AbHiNay".swapcase()) # aBhInAY
