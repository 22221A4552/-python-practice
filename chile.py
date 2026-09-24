from abc import ABC ,abstractmethod
class Ride(ABC):
    def __init__(self,distance):
        self.__distance = distance
    def setdistance(self,distance):
        self.__distance  = distance
    def getdistance(self):
        return self.__distance
    @abstractmethod
    def calculate_fare(self):
        pass
    
class Bike(Ride):
    def calculate_fare(self):
        return self.getdistance()*10

class Car(Ride):
    def calculate_fare(self):
        return self.getdistance()*20

class Customer:
    def __init__(self,name,location):
        self.name = name
        self.location = location


