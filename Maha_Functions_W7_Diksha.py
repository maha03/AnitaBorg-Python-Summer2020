#Coding Challenge:W7:Functions-Diksha
#Mahalakshmi Subramanian
#1.Print reverse of a number
#Accepting input number inside function
def reverse():
    num=(input("Enter a number").rstrip("0"))
    num_list=list(num)
    num_list.reverse()
    return "".join(num_list)
print(reverse())

"""
#Accepting input number from outside function
def reverse(n):
    num_list=list(n)
    num_list.reverse()
    return "".join(num_list)
n=(input("Enter a number").rstrip("0"))
print(reverse(n))
"""

#2.Find square root of a number
import math
def squareroot(n):
    squareroot=math.sqrt(n)
    answer=int(squareroot)
    return answer
n=int((input("Enter a number")))
print(squareroot(n))

""""
#Using command line arguments
import sys,math
def squareroot(n):
    squareroot=math.sqrt(n)
    answer=int(squareroot)
    return answer
print(squareroot(float(sys.argv[1])))
"""
