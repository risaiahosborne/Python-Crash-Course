from car import Car

my_new_car = Car('audi','a4', 2024)
print(my_new_car.describe_name())
my_new_car.odometer_reading= 24
my_new_car.read_odometer()