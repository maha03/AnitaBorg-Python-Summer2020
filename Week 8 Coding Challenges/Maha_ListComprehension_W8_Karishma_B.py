#Coding Challenge:W8:List Comprehension-Karishma
#B.Print List in lexicographic order
#Mahalakshmi Subramanian
p=int(input("Enter cuboid dimension-1 "))
q=int(input("Enter cuboid dimension-2 "))
r=int(input("Enter cuboid dimension-3 "))
N=int(input("Enter an integer"))
#Nested list comprehension with i,j,k values from o to p,q,r and i+j+k: 0 to max i+ max j+max k;
result=[[i,j,k] for i in range(p+1) for j in range(q+1) for k in range(r+1) if i+j+k!=N]
print(result)
