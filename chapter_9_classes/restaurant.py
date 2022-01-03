class Restaurant():

    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.open = False
        self.number_served = 0

    def describe_restaurant(self):
        if self.open:
            print("Welcome to " + self.restaurant_name.title() + "! Where we sever " + self.cusine_type.title() + " food!")
        else: 
            print("At this time "+ self.restaurant_name.title() + " is closed.")
    def open_restaurant(self):
        self.open = True
        print(self.restaurant_name.title() + " Is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

naples = Restaurant("naples", "italian")
old_glory = Restaurant('Old Golory', "american")
drews = Restaurant("Drews bayshore bistro", "cajan")

naples.set_number_served(990)

print(naples.number_served)

naples.increment_number_served(9)

print(naples.number_served)