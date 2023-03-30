from car import Car
from bus import Bus
from all_vehicles import AllVehicles

if __name__ == "__main__":
    auto_park = AllVehicles()
    
    bmw = Car("BMW", "X5", 200, 2.2, 12/100) # price of gas and coeficient of car
    audi = Car("Audi", "A6", 220, 1.8, 16/100) 
    mercedes = Car("Mercedes", "S500", 250, 2.4, 14/100)
    
    fast_bus = Bus("Mercedes", "Sprinter", 120, 30) #number of passengers
    slow_bus = Bus("Ikarus", "Ikarus 260", 80, 50)
    
    all_cars = [bmw, audi, mercedes]
    all_bus = [fast_bus, slow_bus]

    all_vehicles = all_cars + all_bus
    
    for vehicle in all_vehicles:
        auto_park.addVehicle(vehicle)
    
    for vehicle in auto_park.getAllVehicles():
        vehicle.getBrand()
        time_float = vehicle.timeSofiaToBurgas()
        hours, minutes = divmod(time_float * 60, 60)
        hours = round(hours)
        minutes = round(minutes)
        print(f"Time Sofia-Burgas: {hours} hours and {minutes} minutes")
        if isinstance(vehicle, Bus):
            vehicle.getWeightOfPassengers()
        elif isinstance(vehicle, Car):
            vehicle.getPriceForGas()
        print("\n")
        
    print(f"Total vehicles: {auto_park.getNumberOfVehicles()}")
    print(f"Total max speed: {auto_park.sumOfSpeed()}")
    
    
        
