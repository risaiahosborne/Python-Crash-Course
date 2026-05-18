
import json

def ask_if_already_stored(path):
    """Check if user info is already stored."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        print(f"Welcome back, {user_info['name']}! You are {user_info['age']} years old.")
    else:
        get_new_user_info(path)

def get_stored_user_info(path):
    """Get stored user info if available.
    """
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        None
            
def get_new_user_info(path):
    """Prompt for a new user info."""
    name = input("What is your name? ")
    age = input("What is your age? ")
    user_info = {'name': name, 'age': age}
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def user_info():
    """
    Get user info.  
    If so, greet them by name and age. 
    If not, prompt for their name and age and store that information in a file.
    """
    path = path('Chapter 10\\user_info.json')
    user_info = get_stored_user_info(path)

    if user_info:
        print(f"Welcome back, {user_info['name']}! You are {user_info['age']} years old.")
    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_info['name']}!")

user_info()
