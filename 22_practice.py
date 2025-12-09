#Write a recursive function to calculate sum of first n natural number
def Sum(n):
    if(n==1):
        return 1
    else:
        return Sum(n-1)+n
    print(sum(4))