#single inheritance:one parent->one child
class parent:
    def func1(self):
        print("this is function 1")
class child(parent):
    def func2(self):
        print("this is function 2")
c=child()
c.func1()
c.func2()

# #multiple inheritance:multiple parent->one child
class parent1:
    def func1(self):
        print("this is function 1")
        
class parent2:
    def func2(self):
        print("this is function 2")

class child(parent1, parent2):
    def func3(self):
        print("this is function 3")
        print("this is child class")
c=child()
c.func1()
c.func2()
c.func3()     

#multilevel inheritance:grand parent->parent->child
class parent:
    def func1(self):
        print("this is function 1")
class child(parent):
    def func2(self):
        print("this is function 2")
class grandchild(child):
    def func3(self):
        print("this is function 3")
g=grandchild()
g.func1()       
g.func2()
g.func3()  

#Hierarchical inheritance:one parent->multiple children
class parent:
    def func1(self):
        print("this is function 1")
class child1(parent):
    def func2(self):
        print("this is function 2")
class child2(parent):
    def func3(self):
        print("this is function 3")
class child3(parent):
    def func4(self):
        print("this is function 4")
c1=child1()
c2=child2()
c3=child3()

c1.func1()
c1.func2()

c2.func1()
c2.func3()

c3.func1()  
c3.func4()                              


