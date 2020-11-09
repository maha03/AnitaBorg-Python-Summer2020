#Script: special_number.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python program to find whether a number is special or not. A special number is a number composed
#             of only prime digits. Print “True” for  a special number and “False” otherwise.

def specialnumber(num):
    j=1
    for i in num:
        if int(i) in [2,3,5,7]:  #Linear time complexity
            if j==len(num):
                print("True")
            j+=1
            continue
        else:
            print("False")
            break

n=input("Enter a number")
try:
    num=int(n)
    if n<0:
        raise ValueError
except:
    print("Enter valid number")
    exit()

specialnumber(num)