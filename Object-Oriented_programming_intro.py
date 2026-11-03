class Car:

    def __init__(self, company, model, engine):
        self.company = company
        self.model = model
        self.engine = engine

    def info(self):
        return f"Your company is {self.company} and model is {self.model} with {self.engine}!"



car1 = Car("Mahindra", "Thar", "Petrol")
car2 = Car("Maruti", "800", "Petrol")
car3 = Car("TATA", "TATA--", "Petrol/desel")
car4 = Car("Mahindra", "scrpio", "Hybrid")

print(car1.info())
print(car2.info())
print(car3.info())
print(car4.info())





    










