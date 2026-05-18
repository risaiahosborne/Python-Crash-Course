players = ['charles','martina', 'michael', 'florence', 'eli']
print(players[0:3]) #print the first 3
print(players[1:4]) #print 2 to 4
print(players[:4]) #pirnt the first 4
print(players[2:]) #print the 3 to the end
print(players[-3:]) #print the last 3

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    