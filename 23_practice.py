#Write a python function to remove a given word from a list and strip at the same time
l=["Harry","Simran","Rohan","an"]
def rem(l,word):
     n=[]
     for item in l:
          if not(item==word):
          n.append(item.strip(word))
          return n
     print(rem(l,"an"))