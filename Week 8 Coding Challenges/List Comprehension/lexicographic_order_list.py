#Script: lexicographic_order_list.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python program to print List in increasing lexicographic order. Given three integers P,Q and R
#             which represent the dimensions of a cuboid along with an integer N. Print a list of all
#             possible coordinates given by i, j, k on a 3D grid where the sum of (i+j+k) is not equal to N.
#             Here, 0 <= i <=P;0 <= j <= Q; 0 <= k <= R

'''Sample Input
1
1
1
2
Sample Output 0
[[0,0,0], [0,0,1], [0,1,0], [1,0,0], [1,1,1]]
'''

try:
    p=int(input("Enter cuboid dimension-1"))
    q=int(input("Enter cuboid dimension-2"))
    r=int(input("Enter cuboid dimension-3"))
    N=int(input("Enter an integer"))
    if (p or q or r or N) <1:
        raise ValueError
except:
    print("Error.Please enter valid dimensions")
    exit()

#Nested list comprehension with i,j,k values from o to p,q,r and i+j+k: 0 to max i+ max j+max k;
result=[[i,j,k] for i in range(p+1) for j in range(q+1) for k in range(r+1) if i+j+k!=N]
print(result)