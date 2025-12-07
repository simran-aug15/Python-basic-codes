#A spam comment is defined as a text containing following keywords:"Make a lot of money","buy now".write a program to detect spam
p1="Male a lot of money"
p2="Buy now"
message=input("Enter the message ")
if((p1 in message) or (p2 in message)):
    print("spam")
else:
    print("not a spam")    