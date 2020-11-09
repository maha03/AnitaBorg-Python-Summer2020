#Script: common_numbers.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python program that finds common numbers from two lists using list comprehension

try:
    list1 = input("Enter the first sequence of numbers separated by comma")
    if list1.isspace()==False:
        list1=list(map(int,list1.split(',')))
    else:
        raise ValueError
    list2 = input("Enter the second sequence of numbers separated by comma")
    if list2.isspace()==False:
        list2 = list(map(int, list2.split(',')))
    else:
        raise ValueError
except:
    print("Error.Please enter a sequence of numbers separated by comma")
    exit()

common_numbers=[num for num in list1 if num in list2]
print(common_numbers)