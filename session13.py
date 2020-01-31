class song:
    def __init__(self,title,artist,time):
        self.title=title
        self.artist=artist
        self.time=time
        self.nextsong=None
        self.previoussong=None


    def showDetails(self):
        print("song name{}  artist :{} and time{}".format(self.title,self.artist,self.time))



song1 =song(" 1.Bari","momina", 5.25 )
song2=song("2.zinda","raikoti",6.23)
song3=song("3. zalima","arijit",3.30)
song4=song("4 na na","unknown",4.20)
song5=song("5 tum ho","arijit",4.60)

print("1 Bari",song1)
print(("2. zinda",song2))
print("3 zalima",song3)
print("4 na na",song4)
print("tun ho",song5)

# song1.showDetails()
# song2.showDetails()
# song3.showDetails()
# song4.showDetails()
# song5.showDetails()

song1.nextsong=song2
song2.nextsong=song3
song3.nextsong=song4
song4.nextsong=song5
song5.nextsong=song1


song5.previoussong=song4
song4.previoussong=song3
song3.previoussong=song2
song2.previoussong=song1
song1.previoussong=song5


temp=song1

while temp.nextsong !=song1:
    print("-------------")
    temp.showDetails()
    print("------------")
    temp=temp.nextsong


temp.showDetails()
print("________")

current =song5

while current.previoussong != song5:
    print("______________")
    current.showDetails()
    current = current.previoussong
    print("______________")




current.showDetails()
print("_______________")









