#Script: find_value.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A Python program to check whether a specified value is contained in a group of values and return True
#             or False accordingly

''' Sample data:
3 in [1, 5, 8, 3] -> True
-1 in [1, 5, 8, 3] -> False
'''

user_list=input("Enter a sequence of numbers separated by comma")
user_input=input("Enter a number")
try:
    defined_list=user_list.split(',')
    check_number=float(user_input)
    if len(defined_list)>0:
        defined_list = list(map(float, defined_list))
except:
    print("Input a sequence of numbers and number")
    exit()

print(check_number in defined_list)