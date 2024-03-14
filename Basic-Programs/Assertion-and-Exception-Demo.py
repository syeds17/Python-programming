"""Writing a function named DivExp which takes TWO parameter a, b and returns a value c. Writing suitable assertion for a>0 in function DivExp and raising an exception for when b=0."""

import sys

def DivExp(a,b):
    assert a>0, "a  should be greater than 0"
    try:
        c=a/b
    except ZeroDivisionError:
        print("Value of b cammot be zero")
        sys.exit(0)    
    else:
        return c

val_1 = int(input("Enter a value for a : "))
val_2 = int(input("Enter a value for b : ")) 
val_3 = DivExp(val_1,val_2) 
print(val_1,"/",val_2,"=",val_3)      