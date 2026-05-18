motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'BMW'
print(motorcycles)

motorcycles[2] = 'Ford'
print(motorcycles)

motorcycles.append('Saturn')
print(motorcycles)

motorcycles = [ ]

motorcycles.append('Ducati')
motorcycles.append('VW')
motorcycles.append('Ram')

print(motorcycles)

motorcycles.insert(0, 'Porshe')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

del motorcycles[2]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle that I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first bike I owned was a {first_owned.title()}.")

motorcycles = ['BMW', 'Ford', 'Honda', 'Ram']
print(motorcycles)

motorcycles.remove('BMW')
print(motorcycles)

too_expensive = 'Ram'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too rich for my blood.")