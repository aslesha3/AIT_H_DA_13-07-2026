# #*'s instead of vowels in a string
# string="aslesha"
# i=0
# while i<len(string):
#     if string[i] in "aeiou":
#         print("*")
#     else:
#         print(string[i])
#     i+=1

# string=input('enter any string:')
# for i in string:
#     if i in 'aeiouAEIOU':
#         print('*',end=' ')
#     else:
#         print(i,end=' ')


   

# #even and odd numbers from 1 to 100
# #using for loop
# for i in range(1,101):
#     # print(i)
#     print(input("enter a number: "))
#     if i%2==0:
#         print("even number")
#     else:
#         print("odd number")
#     i+=1


# #using while loop
# i=1
# while i<=100:
#     print(i)
#     # print(input("enter a number: ")) ##it shows a number in two ways even and odd
#     if i%2==0:
#         print("even")
#     else:
#         print("odd")   
#     i+=1
    

# #prime numbers from 1 to 100
# #using while loop
# i=1
# while i<101:
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         print(i,end=" ")
#     i+=1

#using for loop
for number in range(2,101):

    count=0 
    for i in range(1,number+1):
        if number%i==0:
            count+=1
    if count==2:
        print(number,"is a prime")
