#Write a program to convert Celsius to Fahrenheit
#C=5*(F-32)/9
def F_to_C(f):
    return 5*(f-32)/9

f=int(input("Enter the temperature"))
print(f"{F_to_C(f)}Degree C")