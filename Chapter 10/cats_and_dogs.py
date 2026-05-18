#Write code ot take town files and print them.

def print_town_file(filename):
    """Print the contents of a town file."""
    try:
        with open(filename) as f: #open the file and assign it to variable f
            contents = f.read() #read the contents of the file and assign it to variable contents
    except FileNotFoundError:
        pass
    else:
        print(contents) #print the contents of the file
    
filenames = [
             'Chapter 10\cats.txt',
             'Chapter 10\dogs.txt'
            ]
for filename in filenames:
    print_town_file(filename)
    
    