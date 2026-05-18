#Generate a list of guests asking for their name and add it to the list. 
from pathlib import Path

guest_list = []

while True:
    name = input('Please enter your name to be added to the guest list (or enter "quit" to finish): ')
    if name == 'quit':
        break
    guest_list.append(name)

path = Path('Chapter 10/guest_book.txt')
path.write_text('\n'.join(guest_list))