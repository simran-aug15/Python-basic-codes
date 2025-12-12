#Write a program to generate multiplication table from 2 to 12 and write it to diff files.


# Write a program to generate multiplication tables from 2 to 12 
# and write each table to different files.

import os

def generatetable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    # Create folder if not exists
    if not os.path.exists("table"):
        os.mkdir("table")

    with open(f"table/table-{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 13):
    generatetable(i)

print("Tables generated successfully!")
