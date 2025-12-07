#Write a program to input eight no from the user and display it
s=set()
for i in range(9):
     n = int(input("Enter the number: "))
     s.add(n)
     
print("The numbers are: ",s)