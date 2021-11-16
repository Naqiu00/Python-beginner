#nested loop = loop inside loop

#make rectangle

# rows = int(input("How many rows? " ))
# columns = int(input("How many columns? " ))
# character = input("What character you want to use?")

# for i in range(rows):
#     for j in range(columns):
#         print(character, end = "")
#     print()

#make a pyramid

base = 0
while base%2 != 1:
    base = int(input("How long you want the pyramid base to be? Use odd number only!!"))
character = input("What character you want to use?")
x = 1
y = 0
for i in range(0, base, 2):
    for z in range(0, (int(base/2)-y)):
        print(" ", end = "")
    for j in range(x):
        print(character, end = "")
    y += 1
    x += 2
    print()