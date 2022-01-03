from car import Car
from electric_car import ElectricCar

my_new_car = Car("ford", "fusion", 2019)
my_new_tesla = ElectricCar("telsla", "s", 2024)

print(my_new_tesla.get_descriptive_name())

my_new_tesla.odometer_reading = 205874
my_new_tesla.battery.describe_battery()