class A:

    a=10

    def __init__(self,a):
        print("A is constructed")
        self.a=a
    def show(self):
        print(" value of a",self.a)
        print("Value of A.a",A.a)

class B:

    B=10

    def __init__(self,b):
        self.b=b
        print("B is constructed")

    def show(self):
        print("Value of B",self.b)
        print("Value of B.b",B.b)

class C(A,B):
    pass

Cref=C(20)
print(Cref.__dict__)

Cref.show()
