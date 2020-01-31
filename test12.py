class Restaurant:

    def __init__(self, name, phone, email, address, pricePerPerson, openingHours, menu):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.pricePerPerson = pricePerPerson
        self.openingHours = openingHours
        self.menu = menu

    def showRestaurant(self):
        print("^^^^^^{}^^^^^^^".format(self.name))
        print("{}\n{}\n{}\n{}\n{}".format(self.phone, self.email, self.address, self.pricePerPerson, self.openingHours))

        self.menu.showMenu()

        print("^^^^^^^^^^^^^^^^^^")


class Menu:

    def __init__(self, name, description, dishes):
        self.name = name
        self.description = description
        self.dishes = dishes

    def showMenu(self):
        print("*****{}*****".format(self.name))
        print(self.description)

        for dish in self.dishes:
            dish.showDish()

        print("*****************")

class Dish:

    def __init__(self, name, price, description, type):
        self.name = name
        self.price = price
        self.description = description
        self.type = type

    def showDish(self):
        print("===={}====".format(self.name))
        print("{}\t{}\t{}".format(self.price, self.description, self.type))
        print("==============")



"""
# Dish Object Construction
dish1 = Dish("Dal Makhani", 200, "Black Lentils Cooked Overnight", "Indian Veg")
dish2 = Dish("Paneer Makhani", 300, "Makhanwala Paneer", "Indian Veg")
dish3 = Dish("Burger", 100, "Tikkiwala Burger", "Indian Veg")
dish4 = Dish("Noodles", 200, "Desi Noodles", "Desi Chinese")
dish5 = Dish("Manchurian", 150, "Gol Gol Manchurian", "Desi Chinese")
# List of Objects
dishes = [dish1, dish2, dish3, dish4, dish5]
# Menu Object Construction
menu = Menu("Sadabahar Menu", "All Indian and Chinese in Short", dishes)
# Restaurant Object Construction
restaurant = Restaurant("IndoChinese", "+91 99999 88888","ic@example.com", "Redwood Shores", 300, "10:00 to 22:00", menu)
