from random import *

Numbers_and_Letters_List = [22, 31, 46, 65, 70, 93, 'L', 'B', 'C', 'W', 'E']

#Randomly select 6 unique numbers and letters from the list for the lottery drawing.
winning_numbers = sample(Numbers_and_Letters_List, 6)

print("Any tickets with the following numbers or letters win a prize:")
for item in winning_numbers:
    print(item)


"""
Lottery Analysis: See how hard it would be to win with a new list called my_ticket 
keep pulling until my ticket wins.
Print a message showing how many times the loop ran until my ticket won.

"""

my_ticket = [22, 'L', 70, 'E', 31, 'C']

winning_numbers = []
attempts = 0

while winning_numbers != my_ticket:
    winning_numbers = sample(Numbers_and_Letters_List, 6)
    attempts += 1
    
print(f"My ticket won after {attempts} attempts!")  

