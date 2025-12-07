#write a program to find out whether a student has passed or failed if it required a total of 40% and least is 33% to pass.assume 3 subjects
marks1=int(input("Enter the marks1: "))
marks2=int(input("Enter the marks2: "))
marks3=int(input("Enter the marks3: "))
total_percentage=100*(marks1+marks2+marks3)/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("pass")
else:
    print("fail")    
