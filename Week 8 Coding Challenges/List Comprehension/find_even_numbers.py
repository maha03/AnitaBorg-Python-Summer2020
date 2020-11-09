##Script: find_even_numbers.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python program to find even numbers from a list of lists of integers using nested list comprehension

import random

#generating list of lists of integers
try:
    number_of_lists=int(input("Enter number of list required"))
    number_of_elements=int(input("Enter number of elements in a list"))
    if number_of_lists>0 and number_of_elements>1:
        list_of_list = [random.sample(range(1, 100), number_of_elements) for i in range(number_of_lists)]
        print("List of list of integers is", list_of_list)
    else:
        raise ValueError
except:
    print("Error. Please enter valid number of lists and number of elements")
    exit()

#using nested list comprehension
even_numbers=[num for sublist in list_of_list for num in sublist if num%2==0]
print("Even numbers in the list of list of integers is",even_numbers)