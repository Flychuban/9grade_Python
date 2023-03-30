from vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, brand, model, max_speed, number_of_passengers):
        self._brand = brand
        self._model = model
        self._max_speed = max_speed
        self._number_of_passengers = number_of_passengers
        self._kmSofia_Burgas = 360

    def getBrand(self):
        print(f"Bus -> Brand: {self._brand} | Model: {self._model}")

    def timeSofiaToBurgas(self):
        time = self._kmSofia_Burgas / self._max_speed
        time = round(time, 2)
        return time

    def getWeightOfPassengers(self):
        person_weight = 75  # number in kilos
        weight = self._number_of_passengers * person_weight
        print(f"All passengers weight: {weight}")
        return weight
    
    def getSpeed(self):
        return self._max_speed
