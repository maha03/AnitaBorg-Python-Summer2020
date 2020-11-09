#Script: reverse_a_number.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A Python program to generate the reverse of a given number N.

def reverse(num):
    num_list=list(str(num))
    num_list.reverse()
    return "".join(num_list)

user_input=(input("Enter a number").rstrip("0"))
try:
    num=int(user_input)
    if num<0:
        raise ValueError
except:
    print("Enter a positive integer")
    exit()

print(reverse(num))