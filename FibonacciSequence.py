"""Developing a program to generate Fibonacci sequance of length(N). Read N from the console."""

num = int(input("Enter the Fibonacci sequence length to be generated : "))  #Input from user

firstTerm=0
secondTerm=1
print("The Fibonacci series with",num,"term is : ")
print(firstTerm,secondTerm,end=" ")
for i in range (2,num):
    curTerm = firstTerm + secondTerm
    print(curTerm,end=" ")
    firstTerm = secondTerm
    secondTerm = curTerm
print()    