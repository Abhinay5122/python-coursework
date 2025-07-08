#4. python operators.py

#1. arithmetic Operators
a=20
b=30
print('addition (a+b):',a+b) # addition (a+b): 50
print('subraction(a-b):',a-b) #subraction(a-b): -10
print('multiplication(a*b):',a*b)# multiplication(a*b): 600
print('divsion(a/b):',a/b)# divsion(a/b): 0.6666666666666666
print('floor divsion(a//b:',a//b)#floor divsion(a//b: 0
print('modulus(a%b):',a%b)#modulus(a%b): 20
print('exponentiation(a**b);',a**b)# exponentiation(a**b); 1073741824000000000000000000000000000000


# 2. comparision operators
c=56
d=23
print('equal to (c==d):',c==d)#equal to (c==d): False
print('not equal to(c!=d):',c!=d)#not equal to(c!=d): True
print('greater than(c>d):',c>d)#greater than(c>d): True
print('less than(c<d):',c<d)#ess than(c<d): False
print('greater than or equal to(c>=d):',c>=d)#greater than or equal to(c>=d): True
print('less than or equal to(c<=d):',c<=d)#less than or equal to(c<=d): False


# Assignment Operators
print( "Asignment operators")
print()
x = 50
print("x",x)
print("addition assignment:",x+10) # addition (a+b): 50
print()
print("subraction assignment:",x-20) # subraction(a-b): -10
print()
print("multiplication assignment:",x*5) # multiplication(a*b): 600
print()
print("division assignment:",x/10) # divsion(a/b): 0.6666666666666666
print()
print("floor division assignment:",x//5) # floor divsion(a//b: 0
print()
print("modulus assignment:",x%5) # modulus(a%b): 20
print()
print("exponention assignment:",x**10) #exponentiation(a**b); 1073741824000000000000000000000000000000


#Logical Operators
print("Logical Operators")
print()
a=10
b=5
print("Logical AND:", a>5 and b<10) # Logical AND: True
print()
print("Logical OR:",a<5 or b>10) # Logical OR: False
print()
print("Logical not:",not(a>5)) # Logical not: False
print(a %2==0) # true
print(b %3==0) # false
print(a %2==0 and b %3==0) # false
print(a %2==0 or b %3==0) # true
print(a %2==0 != b %3==0) # false
 
 
# Membership operators
print("Membership Operators")
print()
str= "Abhinay samrat"
l = [1,2,3,4]
t = [1,2,5,3]
s = [1,2,3,4,5,6,7,8,9]
data ={"name":"abhinay","city": "hyderbad", "roll no" : 197}
print("one is there in l:",1 in l) # one is there in l: True
print("five is not there in l:",5 not in l) # five is not there in l: True
print("five is there in t:",5 in t) # five is there in t: True
print("check using l and t:",1 in l and 1 in t) # check using l and t: True
print("a is there in str:", "a" in str) # a is there in str: True
print("Abhi is there in str:","Abhi"in str) # Abhi is there in str: True
print("zero is there in s:",0 in s) # zero is there in s: False
print("name=abhinay is in data:","name"in data) # name=abhinay is in data: True
print(" city in the data:","city"in data) # city in the data: True
print("school in the data:", "school"not in data) # school in the data: True
print("six is there in the s:",6 in s) # six is there in the s: True

# Identity Operators
print("Identity Operators")
