#OOPS

class Car:
  def __init__(self, window, door, engine):
    self.windows = window
    self.doors= door
    self.enginetype = engine


car1= Car(4,5,"petrol")
print(car1.windows)

car2=Car(6,7,"Diesel")
print(car2.doors)
