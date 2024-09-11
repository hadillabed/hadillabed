class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

name = input("enter your name:")
age=int(input("enter your age:"))
p1=person(name,age)
print(p1.age , p1.name)
del p1.age #delete
print(p1.age)