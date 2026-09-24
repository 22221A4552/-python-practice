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


name = input("enter your customer name :")
location = input("enter your your location")
dis = int(input("enter your distance"))
ride_type =input("enter your ride type")

def ride(dis,ride_type):
    if (ride_type=="bike"):
        distance = dis
        return Bike(distance)
    elif (ride_type == "car"):
        distance = dis
        return Car(distance)
    else:
        print("incoorect")
        return
    
fare=ride(dis,ride_type)
res = fare.calculate_fare()
print(res)