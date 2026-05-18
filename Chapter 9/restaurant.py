class Restaurant:
    """A simple attempt to model a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Return a neatly formatted descriptive name."""
        long_name = (f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
        return long_name.title()

    def open_restaurant(self):
        """Simulate opening the restaurant."""
        print(f"{self.restaurant_name} is now open!")