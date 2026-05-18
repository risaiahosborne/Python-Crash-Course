class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name}!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
class Admin(User):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user'
        ]
        self.privileges_instance = Privileges(self.privileges)  

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
        
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")