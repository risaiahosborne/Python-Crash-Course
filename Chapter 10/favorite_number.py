# Prompts for the user's favorite number
# json.dumps() to store

from pathlib import Path
import json

#favorite_number = input("What is your favorite number? ")
#path = Path('Chapter 10\\favorite_number.json')

#contents = json.dumps(favorite_number)
#path.write_text(contents)

# Write a second prompt that read the value back in and prints the favorite number

#contents = path.read_text()

#favorite_number = json.loads(contents)

#print(f"Your favorite number is {favorite_number}.")

#Repeat this program by mixing the two prompts into a single program that lets the user know if their favorite number is already stored. If it is, it should print the favorite number. If not, it should prompt for the favorite number and store it in a file.

def get_stored_favorite_number(path):
    """Get stored favorite number if available."""
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        return favorite_number
    else:
        None
        
def get_new_favorite_number(path):
    """Prompt for a new favorite number."""
    favorite_number = input("What is your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    return favorite_number

def favorite_number():
    """Get favorite number."""
    path = Path('Chapter 10\\favorite_number.json')
    favorite_number = get_stored_favorite_number(path)

    if favorite_number:
        print(f"Your favorite number is {favorite_number}.")
    elif not favorite_number:
        favorite_number = get_new_favorite_number(path)
        print(f"We'll remember your favorite number when you come back, {favorite_number}!")
    else:
        print("Something went wrong.")

favorite_number()