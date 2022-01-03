class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.current_tank_consumption = 100

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        name = self.get_descriptive_name()
        print("The current miles on your " + name + " : " + str(self.odometer_reading) )

    def drive(self):
        self.odometer_reading += int(input("How many miles? "))

    def set_miles(self, miles):
        if self.odometer_reading < miles:

            self.odometer_reading = miles
        else: 
            print("cant rollback miles!")


class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a battery size of {self.battery_size} -kWh.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)




class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print(f'this car has a {self.battery_size} -kWh battery.')

my_tesla = ElectricCar('tesla', "model s", 2021)

print(my_tesla.get_descriptive_name())
print(my_tesla.battery.describe_battery())
my_tesla.battery.get_range()
        