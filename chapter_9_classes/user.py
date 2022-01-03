class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.loggin_attempts = 0

    def show_info(self, password):
        if password == self.password:
            print(self.username + self.password)
        elif self.loggin_attempts >= 3:
            print("User is locked out. Please reset login_attempts")
        else:
            print("Password is incorrect!")
            self.increment_login_attempts()
            print(self.loggin_attempts)

    def greet_user(self):
        print("Welcome " + self.username)

    def increment_login_attempts(self):
        self.loggin_attempts += 1

    def reset_loggin_attempts(self):
        self.loggin_attempts = 0

me = User("mfg", "asdf")

me.greet_user()

me.show_info("fdsa")
me.show_info("fdsa")
me.show_info("fdsa")
me.show_info("fdsa")




        