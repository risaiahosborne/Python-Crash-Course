from pathlib import Path 
import json

path = Path('nnumbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)