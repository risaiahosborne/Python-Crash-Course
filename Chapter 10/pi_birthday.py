from pathlib import Path

path = Path('Chapter 10\pi_million_digits.txt') # create a Path object that points to the file containing the first million digits of pi

contents = path.read_text().rstrip() # read the contents of the file and remove any whitespace from the right side of the string


for line in contents.splitlines(): # loop through the lines in the file and print each line
    print(line)

pi_string = '' # create an empty string to store the digits of pi in

for line in contents.splitlines(): # loop through the lines in the file and add each line to the pi_string variable, stripping any whitespace from the left side of the line
    pi_string += line.lstrip() # add the line to the pi_string variable, stripping any whitespace from the left side of the line
    
birthday = input("Enter your birhday, in the form mmddyy: ") 
if birthday in pi_string: # check if the user's birthday appears in the pi_string variable
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
    