#Coding Challenge: Sequence types-Chaudhary
#Mahalakshmi Subramanian
#Solution:1
L1=[2,3,4,5,8,4,3,5,2,1,8,8,6,3,4,5,7,9]
str1="hello python three"
#1.Calculate unique elements in L1
unique_elements=(set(L1))
print("No.of unique elements are",len(unique_elements))
#2.Print odd elements only from unique list
solution_list=[]
for ele in unique_elements:
     if ele%2!=0:
         solution_list.append(ele)
print("odd values in list are",solution_list)
#3.Replace, capitalize and store in list
list_str1=[]
str1=str1.replace("three","3")
str1=str1.upper()
list_str1+=[str1]
#4.How tuples are immutable?
"""Tuples are immutable (unchangeable) in the sense we cannot change the elements of tuple once created ie. no append method.we can only access the elements. However, if a tuple is holding a list object, we can make changes to it"""
