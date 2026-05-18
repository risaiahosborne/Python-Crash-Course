Guest_list = ['Jesus', 'Abraham Lincoln', 'Mom', 'Miyamoto Musashi']

print(len(Guest_list))
print(f'{Guest_list[0]}. You have been invited to dinner at my place.')
print(f"You have been invited for dinner, {Guest_list[1]}.")
print(f"{Guest_list[2]}. What are you cooking for dinner?")
print(f"{Guest_list[3]}, try to be on time for dinner!")

print(f"\nSadly, we just found out that {Guest_list[1]} can't make it.")

removed_guest = Guest_list.pop(1)
added_guest = Guest_list.append('Kobe')

print(Guest_list)

print(f"\n{Guest_list[3]}. You are off the bench.")

print(f"\n Letting everyone know we found a bigger table so more people are coming.")

Guest_list.insert(0, 'Kendrick Lamar')
Guest_list.insert(3, 'Evan')
Guest_list.append('James Brown')

print(Guest_list)

print(f"\n{Guest_list[0]}, Hope you can make it from Compton.")
print(f"\n{Guest_list[3]}, Roll up big dawg.")
print(f"\n{Guest_list[6]}, Get on up here!")

print(f"\n Sorry guys only two people can show up.")

James_Brown = Guest_list.pop()
print(f"\n Sorry {James_Brown}, but you didn't make the cut.")
Kobe = Guest_list.pop()
print(f"\n Get home safe {Kobe}.")
Miyamoto_Musashi = Guest_list.pop()
print(f"\n I knew you would understand {Miyamoto_Musashi}.")
Evan = Guest_list.pop()
print(f"\n See you at Christmas {Evan}.")
Kendrick_Lamar = Guest_list.pop(0)
print(f"\n Bet you had a concert to get to {Kendrick_Lamar}.")

print(Guest_list)

del Guest_list[0]
del Guest_list[0]

print(Guest_list)

print(len(Guest_list))
