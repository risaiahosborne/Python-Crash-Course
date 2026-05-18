from user import User

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