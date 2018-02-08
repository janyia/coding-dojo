class Car(object):
    def __init__ (self, price, speed, fuel, mileage, tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax

    def display_all(self):
        print "Price:",self.price
        print "Speed:",self.speed
        print "Fuel:",self.fuel
        print "Mileage:",self.mileage
        print "Tax:",self.tax
        return self

car1 = Car(33000, 125, "Full", 20, 0.15)
car2 = Car(2000, 85, "Half", 18, 0.12)
car3 = Car(8000, 100, "Empty", 25, 0.12)
car4 = Car(7000, 90, "Empty", 24, 0.12)
car5 = Car(6000, 80, "Empty", 23, 0.12)
car6 = Car(5000, 70, "Half", 21, 0.12)

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()