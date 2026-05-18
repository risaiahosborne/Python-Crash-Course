from car import Car, ElectricCar as EC

my_leaf = EC('nissan', 'leaf', 2024)
print(my_leaf.describe_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.describe_name())