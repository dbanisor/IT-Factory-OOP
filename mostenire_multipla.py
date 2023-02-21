class Car:
    def go(self):
        print("vrum vrum")

    def start(self):
        print("starting car")


class Flyable:
    def fly(self):
        print("flu flu")

    def start(self):
        print("starting flyable")


class FlyingCar(Car, Flyable):
    pass


fc = FlyingCar()
fc.fly()
fc.go()
fc.start()  # MRO - method resolution order: se decide care functie din clasa Car sau Flyable se va apela luand de la stanga la dreapta.

print("*" * 50)


# daca vrem sa apelam functiile start() din ambele clase, trebuie redefinit start(), ca mai jos:
class FlyingCar2(Car, Flyable):
    def start(self):
        Car.start(self)
        Flyable.start(self)


fc2 = FlyingCar2()
fc2.start()
