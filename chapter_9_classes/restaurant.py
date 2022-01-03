class Restaurant():

    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.open = False

    def describe_restaurant(self):
        if self.open:
            print("Welcome to " + self.restaurant_name.title() + "! Where we sever " + self.cusine_type.title() + " food!")
        else: 
            print("At this time "+ self.restaurant_name.title() + " is closed.")
    def open_restaurant(self):
        self.open = True
        print(self.restaurant_name.title() + " Is now open!")


naples = Restaurant("naples", "italian")
old_glory = Restaurant('Old Golory', "american")
drews = Restaurant("Drews bayshore bistro", "cajan")

naples.open_restaurant()
naples.describe_restaurant()

old_glory.open_restaurant()
old_glory.describe_restaurant()

drews.describe_restaurant()
drews.open_restaurant()
drews.describe_restaurant()

