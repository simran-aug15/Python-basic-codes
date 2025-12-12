#Write a program to generate multiplication table from 2 to 12 and write it to diff files.


def generateTable(n):
    table=""
for i in range (1,11):
    table += f"{n} X {i}-{n*i}\n" # type: ignore
with open(f"table/table_{i}.txt","w")as f: # type: ignore
    f.write(table)

for i in range(2,13):
    generateTable(i)        
