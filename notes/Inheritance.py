class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name, milage):
        super(Car, self).__init__(name)
        self.engine_statues = False
        self.fuel = 100
        self.milage = milage

    def start_engine(self):
        self.engine_statues = True
        print("You turn the key and the car turns on.")

    def move_forward(self):
        self.fuel -= 1
        print("The car moves forward")

    def turn_left(self):
        self.fuel -= 1
        print("The car turns left,")

    def turn_off(self):
        self.engine_statues = False
        print("You turn off the car")


class Implala(Car):
    def __init__(self):
        super(Implala, self).__init__("Impala", 25)


class KeylessCar(Car):
    def __init__(self):
        super(KeylessCar, self).__init__(name, milage)

    def start_engine(self):
        self.engine_statues = True
        print("You push the button and the car turns on.")


wiebe_car = Keylesscar("Tesla", 125)


jacob_car = Implala()
jacob_car.start_engine()
jacob_car.move_forward()
jacob_car.turn_left()
jacob_car.move_forward()
jacob_car.turn_off()
