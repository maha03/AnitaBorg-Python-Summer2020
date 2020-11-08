class one_D:
    def __init__(self,row,column):
        self.row=row
        self.column=column
    def dot_prod(self,op1):
        op1+=[sum([self.row[i] * self.column[i] for i in range(len(self.column))])]
        print(op1)

class two_D(one_D):
    def __init__(self,a1,a2,b1,b2,op):
        self.a1=a1
        self.a2=a2
        self.b1=b1
        self.b2=b2
        self.op=op
    def dot_prod(self,a1,b1,op):
        super().dot_prod(a1,b1)
        print(op)

# call two_D
childobj=two_D([1,2],[3,4],[5,6],[7,8],[])
print(childobj.op)
