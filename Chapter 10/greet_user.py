from pathlib import Path
import json

path = Path('Chapter 10\\username.json') #Make sure to use the correct path to the username.json file
contents = path.read_text() #Read the contents of the file as a string
username = json.loads(contents) #Use json.loads() to convert the string back into a Python object (in this case, a string)

print(f"Welcome back, {username}!")
