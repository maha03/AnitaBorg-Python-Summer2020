#Script: list_generation.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A Python program which accepts a sequence of comma-separated numbers from the user and generates a list
#             and a tuple with those numbers

'''Sample data: 3, 5, 7, 23
Output:
List: ['3', ' 5', ' 7', ' 23']
Tuple: ('3', ' 5', ' 7', ' 23')
'''

user_input=input("Enter comma seperated values")
if len(user_input)>0:
    output_list=user_input.split(',')
    output_tuple=tuple(output_list)
    print("List is", output_list)
    print("Tuple is", output_tuple)
else:
    print("Input a sequence of numbers")