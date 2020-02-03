class customer_food:
    def __init__(self,burger,chreamBurger):
        self.burger=burger
        self.chreamBurger=chreamBurger

    def showcustomer_food(self):
        print(">>>> Customer Food:{} and {}".format(self.burger,self.chreamBurger))

class upgrade(customer_food):
    def Upgrade(self,fin_fry,Noodle):
        self.fin_fry=fin_fry
        self.Noodle=Noodle

    def showUpgrade(self):

        print(">>>> upgrade food:{}and{} ".format(self.fin_fry,self.Noodle))


cRef=customer_food("Burger1","Burger2")
upgrade1=upgrade("fin_fry","Noodle")

upgrade1.showUpgrade()
cRef.showcustomer_food()


