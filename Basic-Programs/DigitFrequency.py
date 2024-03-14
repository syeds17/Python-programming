"""Developing a program to print the frequency of each digit with suitable massage."""

num = input("Enter a number : ")     #Tking input from user
print("The number entred is : ",num)
uniDig = set(num)
for elem in uniDig:
    print(elem,"occurs",num.count(elem),"times")  #printing the Frequency with suitable massage