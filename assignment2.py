class restorant():
    def __init__(self,menu,dish,price):
        self.menu=menu
        self.dish=dish
        self.price=price

    def showproduct(self):
        print("menu:{}".format(self.menu))
        print("Dish:{}||price:{}".format(self.dish,self.price))

class Menu:
    def __init__(self,name,type,):
        self.name=name
        self.type=type

    def showMenu(self):
        print("name:{}".format(self.name))
        print("Type:{}".format(self.type))

class Dish:
    def __init__(self,name):