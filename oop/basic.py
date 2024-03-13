class Car:
    total_car = 0
    def __init__(self , brand, model):
        self.__brand = brand 
        self.model = model
        Car.total_car+= 1
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    def get_brand(self):
        return f"{self.__brand}"
    def fuel_type(self):
        return "petrol or Diesel"
    
    @staticmethod
    def general_desc():
        return "Cars are means about transport"
# above example about to the Class
# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
# # this is represnting the object

# my_new_car = Car("tata","Safari")
# print(my_new_car.model)

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")
# print(my_tesla.full_name())
#  this is the example of inheritence

# print(my_tesla.get_brand())
#this is the example of encapsulation 
# print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
# print(safari.fuel_type())
print(Car.general_desc())

# this is the example of polymorphsim