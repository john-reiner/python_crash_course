class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_attempts = 0

    def show_info(self, password):
        if password == self.password:
            print(self.username + self.password)
        elif self.login_attempts >= 3:
            print("User is locked out. Please reset login_attempts")
        else:
            print("Password is incorrect!")
            self.increment_login_attempts()
            print(self.login_attempts)

    def greet_user(self):
        print("Welcome " + self.username)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0