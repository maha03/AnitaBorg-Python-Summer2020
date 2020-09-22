#Coding Challenge:W7:Functions-Avichal
#Mahalakshmi Subramanian
num=input("Enter a number")
primenumbers=[2,3,5,7]
def specialnumber():
    j=1
    for i in num:
        if int(i) in primenumbers:  #Linear time cpxity
            if j==len(num):
                print("True")
            j+=1
            continue
        else:
            print("False")
            break
specialnumber()
"""
#using sympy & inbuilt function: problem w/ i value for different length.
import sympy
num=input("Enter a number")
def specialnumber():
    i=0
    if i<len(num):
        while sympy.isprime(num[i]):
            i+=1
    return sympy.isprime(num[i])
print(specialnumber())
"""
