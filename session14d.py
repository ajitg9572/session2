class product:
    def __init__(self,pid,name,price,brand):
        self.pid=pid
        self.name=name
        self.price=price
        self.brand=brand

    def showProductDetail(self):
        print("pid: {} name: {}".format(self.pid,self.name))
        print("price: {}  brand: {}".format(self.price,self.brand))

        print("=============================")

class shoe(product):
    def __init__(self,pid,name,price,brand,shoeSize):
        product.__init__(self,pid,name,price,brand)
        self.shoeSize=shoeSize

    def showShoeDetail(self):
        product.showProductDetail(self)
        print("ShoeSize{}".format(self.shoeSize))
        print("============================")

class mobile(product):
    def __init__(self,pid,name,price,brand,ram,os):
        product.__init__(self,pid,name,price,brand)
        self.ram=ram
        self.os=os

    def showmobileDetail(self):
        product.showProductDetail(self)
        print("ram:{}".format(self.ram))
        print("os is:{}".format(self.os))

class ledTv(product):
    def __init__(self,pid,name,price,brand,screenSize,technology):
        product.__init__(self,pid,name,price,brand,)
        self.screenSize=screenSize
        self.technology=technology
    def showLedDetail(self):
        product.showProductDetail(self)
        print("screenSize::{}".format(self.screenSize))
        print("technology::{}".format(self.technology))

        print("====================================")



Sref=shoe(101,"fling Star",9000,"Adidas",8)
Mref=mobile(202,"samsung galaxy",11000,"samsung",4,"Android")
lref=ledTv(300,"VU smart",30000,"VU",42,"OLED")

Sref.showShoeDetail()
Mref.showmobileDetail()
lref.showLedDetail()
