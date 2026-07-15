#converting into string
#int/integer
i=42  #we cannot convert a char string into int it can only possible for numbers
print(i)
i4=str(i)
print(type(i4),i4)

#float
f=72.45
print(f)
i3=str(f)
print(type(i3),i3)

#bool/boolean
b=True
print(b)
i2=str(b)
print(type(i2),i2)

b2=False
print(b2)
i3=str(b2)
print(type(i3),i3)

#complex
c=5+23j #complex numbers are also not convertable into int
print(c)
i1=str(c)
#i1=int(c) #int() argument must be a string, a bytes-like object or a real number, not 'complex'
print(type(i1),i1)

#converting into integer/int
#string
# a='analytics'
# print(a)
# a1=int(a) #it does not represent a valid number
# print(type(a1),a1)
# so it will shows invalid literal for int() with base 10: 'analytics'

#float
b=15.37
print(b)
b1=int(b)
print(type(b1),b1)

#boolean/bool
c=True
print(c)
c1=int(c)
print(type(c1),c1)

C=False
print(C)
C1=int(C)
print(type(C1),C1)

#complex
# d=15+3j
# print(d)
# d1=int(d) # it must be a string, a bytes-like object or a real number, not 'complex'
# print(type(d1),d1) #so it shows argument error

#converting into boolean
#int
i=12
print(i)
i1=bool(i)
print(type(i1),i1)

#string
s='35'
print(s)
s1=bool(s)
print(type(s1),s1)

F=''
print(F)
F1=bool(F)
print(type(F1),F1)

#float
f=23.45
print(f)
f1=bool(f)
print(type(f1),f1)

#complex
c=13+9j
print(c)
c1=bool(c)
print(type(c1),c1)

#converting into complex
#int
i=73
print(i)
i1=complex(i)
print(type(i1),i1) #<class 'complex'> (73+0j)

#string
# s='hello'
# print(s)
# s1=complex(s) #invalid format
# print(type(s1),s1)

s='42'
print(s)
s1=complex(s)
print(type(s1),s1) #<class 'complex'> (42+0j)

#float 
f=5.37
print(f)
f1=complex(f)
print(type(f1),f1)

#Boolean
b=True
print(b)
b1=complex(b)
print(type(b1),b1)

#converting into float
#int
i=3
print(i)
i1=float(i)
print(type(i1),i1)

#string
#s='typeconversions'
#print(s)
#s1=float(s)
#print(type(s1),s1)

s='4.5'
print(s)
s1=float(s)
print(type(s1),s1)

#Boolean
b=True
print(b)
b1=float(b)
print(type(b1),b1)

b=False
print(b)
b1=float(b)
print(type(b1),b1)

# #complex
# c=3+7j
# print(c)
# c1=float(c) #float argument must be a string or a real number, not complex
# print(type(c1),c1)


