# ask the user for two pieces of information and store them in a dictionary. 
# Then write that dictionary to a file using json.dump().
# Check that the user is the correct user by asking for their name and age. If the name and age match the information stored in the file, print a message welcoming them back. If not, print a message saying that you don't know them.

from pathlib import Path
import json 

def get_stored_user_info(path):
    """Get stored user info if available."""
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
    """Get user info."""
    path = Path('Chapter 10\\user_info.json')
    user_info = get_stored_user_info(path)

    if user_info:
        print(f"Welcome back, {user_info['name']}! You are {user_info['age']} years old.")
    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_info['name']}!")
        
user_info()

