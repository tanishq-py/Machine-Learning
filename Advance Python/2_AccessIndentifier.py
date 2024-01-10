#All the class variables are public
class Car():
  def __init__(self,window,door):
    self.window= window
    self.door= door

audi = Car(5,4)

#all class variables are protected 
class Car():
  def __init__(self,window,door):
    self._window= window
    self._door= door

class Truck(Car):
  def __init__(self,windows,doors,horsepower):
    super().__init__(windows,doors)
    self.horsepower= horsepower

truck1= Truck(5,8,400)
truck=Truck(4,4,4000)
dir(truck)
truck._doors=5
truck._doors

# private
class Car():
    def __init__(self,windows,doors,enginetype):
        self.__windows=windows
        self.__doors=doors
        self.__enginetype=enginetype

audi=Car(4,4,"Diesel")
audi._Car__doors=5
dir(audi)
