class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def fullname(self):
        return f"{self.__brand} {self.__model}"

    @staticmethod
    def general_description():
        return "Cars are means of transportation"

    @property
    def model(self):
        return self.__model

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


    def fuel_type(self):
        return "Electric Charge"

class Battery(ElectricCar):
    def battery_info(self):
        print("this is battery info")

class Engine(ElectricCar):
    def engine_info(self):
        print("this is engine info")

my_new_tesla = ElectricCar("Mahindra", "xuv400", '45kwh')
print(my_new_tesla.battery_size)
print(my_new_tesla.fullname())







# my_tesla = ElectricCar("BYD", "BYD_eMAX_7+", "55KWh")
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))


# # print(my_tesla.fullname())
# # #print(my_tesla.__brand)
# # print(my_tesla.get_brand())
#
#normal_car = Car("Tata", "Safari")
#electric_car = ElectricCar("tesla", "model S",'100kwh')
# print(normal_car.fuel_type())
# print(electric_car.fuel_type())
# Car("Tata", "Safari")
# ElectricCar("tesla", "model S",'100kwh')
# print(Car.total_car)
# my_car = Car("Tata", "Safari")
# #print(my_car.general_description())
# obj = Car("MG",'ZS')
# obj.model = 'combat'
# print(obj.model)

# print(Car.fullname(obj))
# print(obj.model)
# print(Car.general_description())
# print(my_car.general_description())



# my_car = Car("Toyota", "Carolla")
# print(my_car.model)
# print(my_car.brand)
# print(my_car.fullname())
