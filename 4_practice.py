#Write a program to accept the marks of students and display it in sorted manner
marks=[] #empty list
for i in range(5):
   n = int(input("Enter the marks of a student: "))
   marks.append(n)
print("Marks are ",marks)
marks.sort()
print("The sorted list is: ",marks)