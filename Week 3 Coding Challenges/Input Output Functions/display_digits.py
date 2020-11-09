#Script: display_digits.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A program that takes an input as a number. This number strictly needs to be an integer as per the
#             constraints given. The program displays the digits by mathematical operations and not by iterating the
#             number as a python string.
#             Input - Accept an integer as an input where 0 <= N <= 10000
#             Output - Print all the digits of the number from left to right.

"""
Sample Input:
1024
Sample Output:
1
0
2
4
"""

user_input=input("Enter an integer between 0 and 10000").lstrip("0")
try:
    if input <= 0 and input >= 10000:
        input=int(user_input)
        length = len(user_input)
except:
    print("Error!Enter an integer between 0 and 10000")
    exit()
while length>0:
    digit= input // (10 ** (length - 1))
    input= input % (10 ** (length - 1))
    length-=1
    print(digit)