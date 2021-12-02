#Read file and intialize array
dict_array=[]
dict_file = open("C:/Users/bculv/Documents/VS Code/Advent_Directions.txt","r")
for line in dict_file:
    dict_array.append(line.rstrip('\n'))

#Problem One
originX = 0
originY = 0

for direction in dict_array:
    if "forward" in direction:
        originX = originX + int(direction[len(direction) - 1])
    elif "down" in direction:
        originY = originY + int(direction[len(direction) - 1])
    elif "up" in direction:
        originY = originY - int(direction[len(direction) - 1])
print(originX)
print(originY)
print(originX * originY)

#Problem Two
originAim = 0
originX = 0
originY = 0
for direction in dict_array:
    if "forward" in direction:
        originX = originX + int(direction[len(direction) - 1])
        originY = originY + originAim * int(direction[len(direction) - 1])
    elif "down" in direction:
        originAim = originAim + int(direction[len(direction) - 1])
    elif "up" in direction:
        originAim = originAim - int(direction[len(direction) - 1])

print(originY)
print(originX)
print(originX * originY)