#Write a program to find the greatest no entered by user
a1=int(input("Enter the number1: "))
a2=int(input("Enter the number2: "))
a3=int(input("Enter the number3: "))
a4=int(input("Enter the number4: "))
if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is greatest no")
elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greatest no")    
elif(a3>a1 and a3>a2 and a3>a4):
    print("a3 is greatest no")    
elif(a4>a1 and a4>a3 and a4>a2):
    print("a4 is greatest no")    
else:
    print("wrong input")
        
