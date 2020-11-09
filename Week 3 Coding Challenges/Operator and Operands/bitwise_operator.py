#Script: bitwise_operator.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

# DESCRIPTION: A program to find a number from a list that occur odd number of times in O(1) space complexity
#              and O(n) time complexity. The list is defined such that only one number occurs odd number of times

'''Sample Input:
1 2 2 5 5 1 3 9 3 9 6 4 4

Sample Output:
6
'''

user_input=input("Enter a list of numbers separated by space")
num_list=[int(x) for x in user_input.split()]
bit=0
for i in num_list:
    bit=i^bit
print("Number occurring odd number of times is",bit)