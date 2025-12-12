#Write a programto read the following text from a given file"poem.txt"and find out whether it contains the word "Twinkle"
F=open("poem.txt")
content=F.read() 
if("Twinkle"in content):
    print("Yes")
else:
    print("No")
    F.close()    
