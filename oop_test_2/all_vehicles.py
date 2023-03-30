from vehicle import Vehicle

class AllVehicles():
    def __init__(self):
        self._all_vehicles = [] 
        
    def getAllVehicles(self):
        return self._all_vehicles
    
    def addVehicle(self, new_vehicle: Vehicle):
        self._all_vehicles.append(new_vehicle)
    
    def getNumberOfVehicles(self):
        return len(self._all_vehicles)
    
    def sumOfSpeed(self):
        sum = 0
        for vehicle in self._all_vehicles:
            sum += vehicle.getSpeed()
        return sum
    