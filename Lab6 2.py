class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def get_info(self):
        print(f'Марка: {self.make}\nМодель: {self.model}')

class Car(Vehicle):
    def __init__(self,make, model, fuel_type):
        super().__init__(make,model)
        self.fuel_type = fuel_type
    def get_info(self):
        print(f'\nМарка: {self.make}\nМодель: {self.model}\nТип топлива: {self.fuel_type}')

cars = Vehicle('Audi', 'Q8')
car1 = Car('Audi', 'Q8', 'Бензин')
car2 = Car('Audi', 'Q8', 'ДТ')
cars.get_info()
car1.get_info()
car2.get_info()