class Car:
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        
    def drive(self):
        print(f"This {self.model} is driving.")
        
    def stop(self):
        print(f"This {self.model} is stopped.")
        
    