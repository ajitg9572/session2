
#     Restaurant: name, phone, email, address, pricePerPerson, openingHours
#     Menu: name, description
#     Dish: name, price, description,

class Restorant:

    def __init__(self,name, phone, email, address, pricePerPerson, openingHours,Menu):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        self.pricePerPerson=pricePerPerson
        self.openingHours=openingHours
        self.Menu=Menu

    def showRestorent(self):
        print("^^^^^^{}^^^^^^^".format(self.name))
        print("{}\t{}\t{}\t{}".format(self.phone,self.email,self.address,self.pricePerPerson))

        self.menu.showMenu()

        print("^^^^^^^^^^^^^^^^^^")


class Menu:
    def __init__(self,name, description,Dish):

        self.name=name
        self.decription=description
        self.Dish=Dish

    def showMenu(self):
      print("{} {} ".format(self.name,self.decription))

      for dish in self.dishes:
          dish.showDish()

      print("*****************")





class Dish:
    def __init__(self,name, price, description,type):

        self.name=name
        self.price=price
        self.description=description
        self.type=type

    def showDish(self):
        print("===={}====".format(self.name))
        print("{}\t{}\t{}".format(self.price, self.description, self.type))
        print("==============")


dish1=Dish("Dal Makhani",200,"Dal","Indian Food")
dish2=Dish("Burger",20,"Fast Food","Chinese Food")
dish3=Dish("Roti",10,"Bread","Indian Food")


dishes=[dish1,dish2,dish3]


menu=Menu("shada Bahar food","Best deals",dishes)

restorent=Restorant("Ajit Food Hub","9999988888","ajit@example.com","Reshon Shores",300,10,menu)





