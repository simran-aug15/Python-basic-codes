#Write a program to print ***
#                         * *
#                         ***

n=int(input("Enter the number: "))
for i in range(i,n+1):
    if(i==1 or i==n):
     print("*"*n)

else:
   print("*",end=" ")
   print(" "*(n-2),end=" ")
   print("*",end=" ")
   print(" ")     

