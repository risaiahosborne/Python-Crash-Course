from fileinput import filename
from os import path
from pathlib import Path

def count_words(path):
    """Count the number of words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        #If file not found, create a new file missing_files' and add the missing book to the file.
        missing_files = Path("Chapter 10\\missing_files.txt")
        missing_files.write_text(f"{path}\n", encoding="utf-8")
        
    else:
        # Count the approximate number of words in the file.
        words = contents.split() # split() method breaks the string into a list of words.
        num_words = len(words) # len() function counts the number of items in a list, which is the number of words in this case.
        print(f"The file {path} has about {num_words} words.")

filesnames = ["Chapter 10\\siddhartha.txt", "Chapter 10\\moby_dick.txt", "Chapter 10\\alice.txt", 'Chapter 10\\little_women.txt']

for filename in filesnames:
    path = Path(filename)
    count_words(path)