class Car:
    def __init__(self,d,w):
        self.doors=d
        self.seats=4
        self.wheels=w
        self.mirrors=2
    def move(self):
        print("Car is moving at 7km/h")
car=Car(4,4)

print(car.doors)
car.move()