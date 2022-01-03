from restaurant import Restaurant

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cusine_type):
        super().__init__(restaurant_name, cusine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)

