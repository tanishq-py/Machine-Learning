#All vairables are PUBLIC
#car blueprint

class Car():
  def __init__(self,windows,doors,engine):
    self.windows= windows
    self.doors=doors
    self.engine=engine
  def drive(self):
    print("the person drives the car")

dir(Car)

class Audi(Car):
  def __init__(self,windows,doors,engine,enableAI):
    super().__init__(windows,doors,engine)
    self.enableAI= enableAI
  
  def selfdrive(self):
    print("audi supports self driving")

audiQ7= Audi(5,5,"diesel",True)
audiQ7.windows
