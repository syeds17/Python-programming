"""Developing a python program to calculate binomial coefficient (Given N and R)"""

def fact(num):  #Defining a function to calculate factorial of a number
    if num == 0:
        return 1
    else:
        return num * fact(num-1)
#Input from user    
n = int(input("Enter the value of N : ")) 
r = int(input("Enter the value of R : "))
assert  r < n,  "R cannot be greater than N"  #Raising an assertion
if r<=0:
    print("R cannot be less than or equal to zero")
nCr = fact(n)/(fact(r)*fact(n-r))
print(n,'C',r,"=","%d"%nCr,sep="")