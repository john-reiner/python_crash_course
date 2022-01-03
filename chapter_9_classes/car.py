class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

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

truck = Car('Chevy', "silverado", 2021)

truck.odometer_reading = 21

truck.drive()

truck.set_miles(1000)

print(truck.read_odometer())
        