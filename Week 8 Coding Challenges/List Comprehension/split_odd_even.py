##Script: split_odd_even.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python program using single list comprehension that takes one input list and
#             returns two lists; one for even and another for odd numbers.

import random

try:
    user_input=int(input("Enter the number of elements in list"))
    if user_input>=1:
        num_of_elements=user_input
    else:
        raise ValueError
except:
    print("Error.Please enter a positive integer")
    exit()

user_list=random.sample(range(1,100),num_of_elements)

even,odd=[],[]
even=[i for i in user_list if i%2==0 or odd.append(i)]
print("Even numbers in list are",even,"\n" "Odd numbers in list are",odd)