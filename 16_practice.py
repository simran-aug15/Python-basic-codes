#Writeba program to calculate the factorial using for loop
n = int(input("Enter the number: "))
i=1
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial is:",fact)    