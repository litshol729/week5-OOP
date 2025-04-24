class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving")

class MotorBike(Vehicle):
    def move(self):
        print("Driving")

class Bus(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

vehicles = [Car(), MotorBike(), Bus(), Plane()]
for v in vehicles:
    v.move()