#print the digits in a number
number=int(input("enter any number: "))
while number>0:
    res=number%10 ##4,##3,##2,##1
    print(res)
    number=number//10  ##number=1234//10=123, number=123//10=12, number=12//10=1, number=1//10=0


#Sum of the digits in a number
sum=0
while number>0:
    result=number%10
    sum+=result
    number//=10
print(sum)

#traverse through a string
string="AchieversIT"
i=0
while i<len(string):
    print(string[i])
    i+=1


#palindrome of a number
number=121
dup=number
reverse=0
while number>0:
    res=number%10 #121%10=1, 12%10=2, 1%10=1
    reverse=reverse*10+res #0*10+1=1, 1*10+2=12, 12*10+1=121
    number//=10 #121//10=12, 12//10=1, 1//10=0
    # print(reverse) #False
   
if dup ==reverse:
    print(dup,'is a palindrome')
else:
    print(dup,'is not a palindrome')



#1.palindrome of a string
string="madam"
i=len(string)-1
reverse=""
while i>=0:
    print(string[i])
    i-=1

#2.
string="AchieversIT"
i=len(string)-1
reverse=''
while i>=0:
    chr=string[i]
    reverse+=chr
    i-=1
if string==reverse:
    print(string,'is a palindrome')
else:
    print(string,'is not a palindrome')


#Factor
number=10
i=1
count=0
while i<number:
    if number%i==0:
        print(i)
        count+=1
    i+=1
print('the factors of a number',number,'is: ',count)


#prime or not
num=int(input('enter any number: '))
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print(num,'is a prime')
else:
    print(num,'is not a prime')
    
        
    
