#Use the count method to fime how many words are in a string from text files. 

filename = 'Chapter 10\moby_dick.txt'

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f: 
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        #Count the approximate number of words in the file.
        occurances = contents.lower().count('the') 
        print(f"The file {filename} has 'the' about {occurances} times.") 
        
count_words(filename)