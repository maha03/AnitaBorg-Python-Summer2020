#Coding Challenge:W8:Lambdas -Srivalya Elluru
#Mahalakshmi Subramanian
def fib(n):
    sol_list=[0]
    while len(sol_list)<n:
        length=len(sol_list)
        if length==1:
            sol_list+=[sol_list[length-1]+1]
        else:
            sol_list+=[sol_list[length-1]+sol_list[length-2]]
    return sol_list
n=int(input("Enter length of Fibonacci series"))
fibonacci_list=fib(n)
fibonacci_squared=list(map(lambda x:x**2,fibonacci_list))
print(fibonacci_squared)
