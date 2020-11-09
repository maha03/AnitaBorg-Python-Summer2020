#Script: range_validation.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A Python program to test whether a number is within 100 of 1000 or 2000

user_input=input("Enter a number")
try:
    check_num=float(user_input)
except:
    print("Input a number")
    exit()
if check_num>=1000:
    if((abs(1000-check_num)>0.0) and (abs(1000-check_num)<100.0)):
        print("The number is within 100 of 1000")
    elif((abs(2000-check_num)>0.0) and (abs(2000-check_num)<100.0)):
        print("The number is within 100 of 2000")
    else:
        print("The number is neither within 100 of 1000 or 2000")
else:
    print("The number is neither within 100 of 1000 or 2000")