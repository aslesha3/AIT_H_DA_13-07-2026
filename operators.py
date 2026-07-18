#Arithematic operators
a=5
b=7
print(a+b)

a='Aslesha'
b='Chintha'
print(a+b) # addition is used for strings that are accepted for concatenation

a=5
b=7
print(a/b) # division operator shows the result in float

a=5
b=10
print(a//b) # floor division operator shows the result as an integer

a=5
b=10
print(a%b) # modulo operator shows the remainder of the division

a=5
b=2
print(a**b) # exponentiation operator shows the result of raising a to the power of b

#Assignment operators
a=5
print(id(a),a)
a+=5 # a=a+5, a=5+5, a=10
print(id(a),a) # id of a is changed because it is immutable
a-=5 # a=a-5, a=10-5, a=5
print(a)
a*=4 # a=a*4, a=5*4, a=20
print(a)
a//=2 # a=a//2, a=20//2, a=10
print(a)
a/=2 # a=a/2, a=10/2, a=5.0
print(a) 
a**=2 # a=a**2, a=5**2, a=25
print(a)

#comparision operators
a=5
b=10
print(a==b) ## False #results will be in boolean values True or False
print(a!=b) # True
print(a>b) # False
print(a<b) # True
print(a>=b) # False
print(a<=b) # True

#logical operators
a=10
b=20
print(a>5 and b>30) # False , Performs on two comparision operators and returns True if both are True, otherwise returns False
print(a>5 or b>30) # True , returns True if at least one of the operators is True, otherwise returns False
print(not(a>5)) # False , returns the opposite of the boolean value of the expression
print(not(b>25)) # True , returns the opposite of the boolean value of the expression

#Membership operators
a="Aslesha"
print("A" in a) # True

l=[1,2,3,4,5]
print(3 in l) # True
print(5 not in l) # False 

#identity operators
a=10
b=10
print(a is b) # True , returns True if both variables point to the same object in memory, otherwise returns False
a=10
b=10
print(a is not b) # False