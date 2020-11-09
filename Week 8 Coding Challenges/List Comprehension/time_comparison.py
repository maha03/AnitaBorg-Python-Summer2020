#Script: time_comparison.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python program to compare time required for 'for loop' and 'list comprehension' execution

import timeit,random

input_1=random.sample(range(1, 100), 8)
input_2=random.sample(range(1, 100), 8)

#using for loop
print("Time using for loop in seconds is",timeit.timeit('''
def usingfor():
    common_numbers=[]
    for i in input_1:
        if i in input_2:
            common_numbers.append(i)'''))

#using list comprehension
print("Time using list comprehension in seconds is",timeit.timeit('''
def usinglistcomprehension():
    common_numbers=[num for num in input_1 if num in input_2]'''))