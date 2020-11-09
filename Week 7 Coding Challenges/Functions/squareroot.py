#Script: squareroot.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A Python program to find the square root of a number and return the integral part only

'''Sample Input : 10
Sample Output : 3
'''

import math
def squareroot(n):
    squareroot=math.sqrt(n)
    answer=int(squareroot)
    return answer

user_input=input("Enter a number")
try:
    n=int(user_input)
    if n<0:
        raise ValueError
except:
    print("Enter a valid number")
    exit()

print(squareroot(n))