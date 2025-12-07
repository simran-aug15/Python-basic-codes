#Write a program to calculate the grade of a student from his marks
a=int(input("Enter the marks: "))
if(a<=100 and a>90):
    print("A grade")
elif(a<=90 and a>80):
    print("B grade")
elif(a<=80 and a>70):
    print("C grade")
elif(a>=70 and a<60):
    print("d grade")
elif(a<=60 and a>50):
    print("E grade")
else:
    print("Fail")        

