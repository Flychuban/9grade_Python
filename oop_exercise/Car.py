class Car():
    def __init__(self, brand, model, year, price, color) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.color = color
    
    def __str__(self) -> str:
        return f"{self.brand} {self.model} {self.year} {self.price} {self.color}"
    
    def start_car(self):
        print(f"{self.brand} {self.model} is starting")
    
    def stop_car(self):
        print(f"{self.brand} {self.model} is stopping")
    