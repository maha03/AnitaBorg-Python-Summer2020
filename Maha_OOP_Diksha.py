#2
class Student:
    name="Rohan"
    age=16
s1=Student()
s2=Student()
print(s1.name,end=" ")
print(s1.name,end=" ")

#3-getattr(),setattr()
class change:
    def __init__(self,x,y,z):
        self.a=x+y+z
x=change(1,2,3)
y=getattr(x,'a')
setattr(x,'a',y+1)
print(x.a)

#4-private variable
class A:
    def __init__(self):
        self.x=1
        self.__y=1
    def getY(self):
        return self.__y
a=A()
a.__y=45
print(a.getY())

#5-default vs parametrized constr.
class example():
    def __init__(self,a):
        self.x=a
a=example()
