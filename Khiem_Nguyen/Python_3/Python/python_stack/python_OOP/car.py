class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print("Price:" + str(self.price))
        print("Speed:" + str(self.speed) + "mph")
        print("Fuel:" + str(self.fuel))
        print("Mileage:" + str(self.mileage) + "mpg")
        print("Tax:" +str(self.tax))

car1 = Car(2000, 35, "Full", 15)
car1 = Car(2000, 5, "Not Full", 105)
car1 = Car(2000, 15, "Kind of Full", 95)
car1 = Car(2000, 25, "Full", 25)
car1 = Car(2000, 45, "Empty", 25)
car1 = Car(20000000, 35, "Empy", 15)