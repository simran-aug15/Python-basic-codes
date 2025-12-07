#create an empty dictionary .allow 4 friends to enter their fav. language as value and key
d={}
for i in range(5):
     name=input("Enter the name: ")
     lang=int(input("Enter the language: "))
     d.update({name:lang})
print(d)    