from car import Car
from bus import Bus

if __name__ == "__main__":
    bmw = Car("BMW", "X5", 200, 2.2, 12/100) #price of gas and coeficient of car
    audi = Car("Audi", "A6", 220, 1.8, 16/100)
    mercedes = Car("Mercedes", "S500", 2.4, 250, 14/100)
    
    fast_bus = Bus("Mercedes", "Sprinter", 120, 30) #number of passengers
    slow_bus = Bus("Ikarus", "Ikarus 260", 80, 50)  
      
    all_cars = [bmw, audi, mercedes]
    all_bus = [fast_bus, slow_bus]
    
    all_vehicles = all_cars + all_bus
    
    for vehicle in all_vehicles:
        vehicle.getBrand()
        print(f"Time Sofia-Burgas: {vehicle.timeSofiaToBurgas()}")
        if isinstance(vehicle, Bus):
            vehicle.getWeightOfPassengers()
        elif isinstance(vehicle, Car):
            vehicle.getPriceForGas()
        print("\n")