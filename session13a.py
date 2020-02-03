class Dish:

    def __init__(self,name,price,description,type):
        self.name=name
        self.price=price
        self.description=description
        self.type=type
        self.quantity=0
    def showDetail(self):
        print("======={}========".format(self.name))
        print("price:{},description:{} ,type:{} and quantity:{}".format(self.price,self.description,self.type,self.quantity))




dish1=Dish("Dal Makhani",100,"well prepared","indian food")
dish2=Dish("burger",20,"well prepared","chinese food")
dish3=Dish("Roti",10,"well prepared","indian Bread")
dish4=Dish("Noodle",50,"well prepared","chinese")
dish5=Dish("Manchurian",70,"well prepared","chinese")


# dish1.showDetail()
# dish2.showDetail()
# dish3.showDetail()
# dish4.showDetail()
# dish5.showDetail()


cart =[]
total_dishes=0

def addtocart(dish):
    global total_dishes
    cart.append(dish)
    total_dishes +=1

dish1.quantity=2
dish2.quantity=2
dish5.quantity=1



addtocart(dish1)
addtocart(dish2)
addtocart(dish5)


total_price=0
total_item=0

for dish in cart:
    dish.showDetail()
    total_price +=(dish.price+dish.quantity)
    total_item +=dish.quantity


print(">> Total Price:\u20b9", total_price)
print(">> Total Items:", total_item)
print(">> Total Dishes:", total_dishes)


