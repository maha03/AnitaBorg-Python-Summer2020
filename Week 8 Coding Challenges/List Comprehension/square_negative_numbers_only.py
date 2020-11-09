#Script: square_negative_numbers_only.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python program to square negative numbers from input list and leave positive numbers as it is

'''Sample Input:
2 -3 4 5 -1
Sample Output:
[2, 9, 4, 5 ,1 ]
'''

user_input=input("Enter a list of numbers separated by space")
try:
    input_list=user_input.split()
    if len(input_list)>0:
        input_list = list(map(int,input_list))
    else:
        raise ValueError
except:
    print("Error. Please enter list of numbers separated by space")
    exit()

#squaring only negative numbers in the list
result=[i**2 if i<0 else i for i in input_list]
print(result)