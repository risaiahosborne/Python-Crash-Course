my_foods = ['pizza', 'chips', 'soda']
friend_foods = my_foods[:]

my_foods.append('ice cream')
friend_foods.append('salad')

print("My favorite foods are.")
print(my_foods)

print("\nMy friend's favorites are.")
print(friend_foods)

#4-10
print("\n The first three items in the lst are:")
print(my_foods[:3])

print("\n Two items from the middle of the list:")
print(my_foods[1:3])

print("\n The last item in the list is.")
print(my_foods[-1])

pizza = ['pepperoni', 'cheese', 'bbq chicken', 'meat lovers']
friend_pizza = pizza[:]

pizza.append('veggie')
friend_pizza.append('hawaiian')

print("\n My favorite pizzas are:")
print(pizza)

print("\n My friend's favorite pizzas are:")
print(friend_pizza)

for food in my_foods:
    print("\nI really love " + food + "!")  