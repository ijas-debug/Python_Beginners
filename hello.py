a = "hi, how are you?"

print(len(a))

print(a[5])

print(a[4:8])
print(a[-6:-1])

players = ["Messi", "Maria", "De paul"]  # String is immutable
players[1] = "Enzo"  # list is mutable
print(players)
print(len(players))
print(players[0])
print(players[0:])

players = players + ["Marti", "Romero"]
print(players)

players.append("Vamos") #value add to last postn
print(players)

players.append(input("enter a name"))
print(players)


