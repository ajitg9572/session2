class parent:
    vahicle="PB10EU5905"

    def __init__(self,fname,lname,wealth):
        self.fname=fname
        self.lname=lname
        self.wealth=wealth

    def showDetail(self):
     print("{}|{}|{}|{}".format(self.fname,self.lname,self.wealth,parent.vahicle))

class child(parent):
    vahicle="KBC101010"

    def __init__(self,name,salary):
       self.name=name
       self.salary=salary

    def showDetail(self):
        print("{}|{}|{}".format(self.name,self.salary,child.vahicle))

    def show(self,ref):
        print("{}|{}|{}".format(self.name,self.salary,child.vahicle))
        parent.showDetail(ref)


cref=child("ajit kumar",30000)

print(">>>",child.__dict__)
print(">>>>>",cref.__dict__)


pref=parent("ajit","gupta",300000)
pref.showDetail()


cref.show(pref)











