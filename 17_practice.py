#Write a program to print following  pattern    *
#                                              ***
#                                             *****

n=int(input("Enter the n: "))
for i in range(i,n+1):
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1),end=" ")
    print(" ")