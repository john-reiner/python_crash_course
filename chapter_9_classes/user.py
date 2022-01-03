class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def show_info(self, password):
        if password == self.password:
            print(self.username + self.password)
        else:
            print("Password is incorrect!")

    def greet_user(self):
        print("Welcome " + self.username)

me = User("mfg", "asdf")
me.greet_user()



        