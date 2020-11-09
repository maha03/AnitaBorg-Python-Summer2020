#Coding Challenge:W8:List COmprehension -Karishma
#A.Small coding problems solutions
#Mahalakshmi Subramanian
import timeit,random
#1.Removing vowels from a sentence
text=input("Enter a string").strip()
vowel_list=['a','e','i','o','u']
text_consonant=[i for i in text if i not in vowel_list]
print("".join(text_consonant))

#2.Finding common numbers
a=list(input("Enter a sequence of numbers"))
b=list(input("Enter a sequence of numbers"))
common_numbers=[i for i in a if i in b]
print(common_numbers)

#3.Time for comprehension vs. for loop
a=random.sample(range(1,100),8)
b=random.sample(range(1,100),8)
print("Time using for loop is",timeit.timeit('''
def usingfor():
    common_numbers=[]
    for i in a:
        if i in b:
            common_numbers.append(i)'''))
print("Time using list comprehension is",timeit.timeit('''
def usinglistcomprehension():
    common_numbers=[i for i in a if i in b]'''))

#4.Make a single list comprehension to return two lists, one for even and another for odd numbers.
num_of_elements=int(input("Enter the number of elements in list"))
user_list=random.sample(range(1,100),num_of_elements)
print(user_list)
even,odd=[],[]
#using list comprehension with if condition and 'or' for else condition
#even=[i if int(i)%2==0 else odd.append(i) for i in user_list ] None is appended for odd elements in even list
#even=[i if int(i)%2==0 or odd.append(i) for i in user_list ] Invalid syntax error
even=[i for i in user_list if i%2==0 or odd.append(i)]
print("Even numbers in list are",even,"\n" "Odd numbers in list are",odd)

#5.find even numbers from a list of lists of integers using nested list Comprehension
num_of_list=int(input("Enter number of list required"))
num_of_elements=int(input("Enter number of elements in a list"))
list_of_list=[random.sample(range(1,100),num_of_elements) for i in range(num_of_list)]
print("List of list of integers is",list_of_list)
#using nested list comprehension similar to nested loops: sublist : list within list_of_list
even_numbers=[i for sublist in list_of_list for i in sublist if i%2==0]
print("Even numbers in the list of list of integers is",even_numbers)
