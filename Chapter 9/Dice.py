from random import*

class Die:
    """A class representing a single die."""
    
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
        
    def roll_die(self):
        """Return a random value between 1 and the number of sides."""
        return randint(1, self.num_sides)
    
# Create a 6-sided die and roll it 10 times.
die = Die()
print("Rolling a 6-sided die:")
for _ in range(10):
    print(die.roll_die())
# Create a 10-sided die and roll it 10 times.
die10 = Die(num_sides=10)
print("Rolling a 10-sided die:")
for _ in range(10):
    print(die10.roll_die())
# Create a 20-sided die and roll it 10 times.
die20 = Die(num_sides=20)
print("Rolling a 20-sided die:")
for _ in range(10):
    print(die20.roll_die())