from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, brand, model, max_speed, price_of_gas, coeficient_of_car):
        self._brand = brand
        self._model = model
        self._max_speed = max_speed
        self._price_of_gas = price_of_gas
        self._kmSofia_Burgas = 360
        self._coeficient_of_car = coeficient_of_car

    def getBrand(self):
        print(f"Car -> Brand: {self._brand} | Model: {self._model}")

    def timeSofiaToBurgas(self):
        time = self._kmSofia_Burgas / self._max_speed
        time = round(time, 2)
        return time

    def getPriceForGas(self):
        used_liters = self._coeficient_of_car * self._kmSofia_Burgas
        price = used_liters * self._price_of_gas
        price = round(price, 2)
        print(f"The price for gas is: {price}")
        return price

    def getSpeed(self):
        return self._max_speed