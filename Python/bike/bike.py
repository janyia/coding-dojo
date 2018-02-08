class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price=price
        self.max_speed=max_speed
        self.miles=miles

    def displayinfo(self):
        print "The price is:",self.price
        print "The maximum soeed is:",self.max_speed
        print "The total miles are:",self.miles
        return self
    def ride(self):
        self.miles +=10
        print "Riding",self.miles
        return self

    def reverse(self):
        self.miles -=5
        print "Reversing",self.miles
        return self

bike1= Bike(500, 25, 10)
bike2= Bike(300, 15, 10)
bike3 = Bike(200, 10, 10)

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayinfo()


