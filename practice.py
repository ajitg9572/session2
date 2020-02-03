class product:
    def __init__(self,pid,name,price,brand):
        self.pid=pid
        self.name=name
        self.price=price
        self.brand=brand

    def showproduct(self):
        print("pid:{}".format(self.pid))
        print("name:{} || price:{}".format(self.name,self.price))
        print("brand:{}".format(self.brand))

class shoe(product):
    def __init__(self,pid,name,price,brand,size):
        product.__init__(self,pid,name,price,brand)
        self.size=size

    def showShoeDetail(self):
        product.showproduct(self)
        print("Size",self.size)
        print("====================")

class mobile(product):
    def __init__(self,pid,name,price,brand,ram,os):
        product.__init__(self,pid,name,price,brand)

        self.ram=ram
        self.os=os

    def showMobileDetail(self):
        product.showproduct(self)
        print("ram",self.ram)
        print("os:",self.os)
        print("=========================")

class ledTv(product):
    def __init__(self,pid,name,price,brand,screenSize,Technology):
        product.__init__(self,pid,name,price,brand)
        self.screenSize=screenSize
        self.Technoogy=Technology

    def showLedDetail(self):
        product.showproduct(self)
        print("screen Size",self.screenSize)
        print("Technology",self.Technoogy)
        print("==========================")




Sref=shoe(101,"flying king",8000,"Adidas",9)
Mref=mobile(200,"NOkia-101",8900,"Nokia",4,"Android")
lref=ledTv(310,"VU smart",59000,"VU",50,"Oled")


Sref.showShoeDetail()
Mref.showMobileDetail()
lref.showLedDetail()

