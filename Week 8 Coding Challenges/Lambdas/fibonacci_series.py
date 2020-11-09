#Script: fibonacci_series.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python program to generate a list of the first n Fibonacci numbers,0 being the first number. Then, using
#             map function and a lambda expression, it squares each Fibonacci number and print the list.

'''Sample Input:6
Sample Output: [0, 1, 1, 4, 9, 25]
'''

def fib(n):
    sol_list=[0]
    while len(sol_list)<n:
        length=len(sol_list)
        if length==1:
            sol_list+=[sol_list[length-1]+1]
        else:
            sol_list+=[sol_list[length-1]+sol_list[length-2]]
    return sol_list

#receiving user input and checking the input value
user_input=input("Enter length of Fibonacci series")
try:
    n=int(user_input)
    if n<1:
        raise ValueError
except:
    print("Enter length greater than 0")
    exit()

#call to fib() to obtain list
fibonacci_list=fib(n)

#using map and lambda expression to square the numbers in list
fibonacci_squared=list(map(lambda x:x**2,fibonacci_list))
print(fibonacci_squared)
