class Dog():
    """A simple attempt to model a dog."""
    

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name 
        self.age = age
        self.ex_points = 0

    def sit(self):
        """Simulates a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting!")

    def roll_over(self):
        """Simulate rolling over in a response to a command."""
        print(self.name.title() + " rolled over!")

    def train(self):
        self.ex_points += 1