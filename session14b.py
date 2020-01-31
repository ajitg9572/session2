class parent:

    vahicle="Pb10eyvg"

    def __init__(self,fname,lname,wealth):
        self.fname=fname
        self.lname=lname
        self.wealth=wealth


class child(parent):
    pass


print("Dictionary of Child")
print(child.__dict__)


Cref=child("ajit","gupta",900000)

print("Dictionary of Cref")
print(Cref.__dict__)

print(">>>>> Vahicle of parent Class",Cref.vahicle)

