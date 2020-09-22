#Coding Challenge:W3:Input & output functions-Kamran
#Mahalakshmi Subramanian
#w/o list to store values
user_input=input("Enter an integer between 0 and 10000").lstrip("0")
num=int(user_input)
n=len(user_input)
while n>0:
    sol=num//(10**(n-1))
    num=num%(10**(n-1)) #modulo would give the number without the nth digit
    n-=1
    print(sol)
'''    
#w/o divmod but using both // and %
user_input=input("Enter an integer between 0 and 10000")
n=len(user_input)
num=int(user_input)
sol=[]
while n>0:
    sol+=[num//(10**(n-1))]
    num=num%(10**(n-1)) #modulo would give the number without the nth digit
    n-=1
for i in range(len(sol)):
    print(sol[i],sep="\n")


#using divmod()
user_input=input("Enter an integer between 0 and 10000")
n=len(user_input)
num=int(user_input)
quotient=[]
while n>0:
    a=divmod(num,10**(n-1))
    quotient+=[a[0]]
    num=a[1] #reminder would become the next number
    n-=1
for i in range(len(quotient)):
    print(quotient[i],sep="\n")
'''
