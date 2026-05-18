from pathlib import Path # import the Path class from the pathlib module, which provides an object-oriented interface for working with file paths

content = 'Hello, World!\n' 
content += 'Change the world!\n'
content += 'You can do it!\n'

path = Path('Chapter 10\programming.txt') # create a Path object that points to the file containing the message to be written

path.write_text(content) # write the string 'Hello, World!' to the file specified by the path object, overwriting any existing content in the file
