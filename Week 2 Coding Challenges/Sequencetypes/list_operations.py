#Script: list_operations.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python program that calculates how many unique elements are in the input list, prints its odd elements,
#             and replaces a string with its corresponding numerical value, capitalizes and store the string in a list

input_list=[2, 3, 4, 5, 8, 4, 3, 5, 2, 1, 8, 8, 6, 3, 4, 5, 7, 9]
input_string= "hello pytHon three"

#Calculate unique elements in input list
unique_elements=(set(input_list))
print("No.of unique elements are",len(unique_elements))

#Print odd elements only from unique list
solution_list=[]
for ele in unique_elements:
     if ele%2!=0:
         solution_list.append(ele)
print("odd values in list are",solution_list)

#Replace, capitalize and store in list
input_string=input_string.replace("three", "3")
input_string=input_string.upper()
new_list=[input_string]
print(new_list)