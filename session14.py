class A:

    a=10

    def __init__(self,b):
        print(">>> object oriented constructed Of A ")
        self.b=b

class B:

    def __init__(self,y):
        print(">>> object Oriented Programming of B")
        self.y=y

class C(A,B):
    pass

cRef=C(10)
print(cRef.__dict__)

cRef.show()



