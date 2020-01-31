class Counter:
    scount=1

    def __init__(self):
        self.count=1

    def increment(self):
        self.count +=1

        Counter.scount +=1

    def decrement(self):
        self.count -=1

        Counter.scount -=1

    def showCounter(self):

        print("self count is {} and scount{}".format(self.count,Counter.scount))


c1 =Counter()
c2=Counter()
c3=c1

c1.increment()
c1.increment()
c2.increment()
c3.increment()


c1.decrement()
c3.decrement()
c2.decrement()

c1.showCounter()
c2.showCounter()
c3.showCounter()


