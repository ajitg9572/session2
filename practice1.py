class Dish:
    def __init__(self,name,price,decription,type):
        self.name=name
        self.price=price
        self.decription=decription
        self.type=type
        self.quantity=0

    def showDish(self):
        print("Name:{}".format(self.name))
        print("price:{}||Decription:{}".format(self.price,self.decription))
        print("Type:{}".format(self.type))
        print("===========================")

dish1=Dish("Dal Makhhni",100,"Launch","Indian Veg")
dish2=Dish("chicken masala",450,"launch","Indian Non-veg")
dish3=Dish("Butter Checken",500,"launch","Indian Non-veg")
dish4=Dish("Butter Panner",350,"launch","Indian Veg")

dishes=[dish1,dish2,dish3,dish4]
# dish1.showDish()
# dish2.showDish()
# dish3.showDish()
# dish4.showDish()

cart=[]
total_dish=0

def addtocart(dish):
    total_dish=total_dish + quantity


