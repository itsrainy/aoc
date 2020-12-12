import math
file1 = open('input.txt', 'r') 
dirs = [s.strip() for s in file1.readlines()]

ship_x = 0.0
ship_y = 0.0
ship_heading = 0.0 # degrees

for d in dirs:
    direction = d[0]
    units = int(d[1:])
    if direction == "E":
        ship_x += units
    elif direction == "W":
        ship_x -= units
    elif direction == "N":
        ship_y += units
    elif direction == "S":
        ship_y -= units
    elif direction == "L":
        ship_heading += units
    elif direction == "R":
        ship_heading -= units
    elif direction == "F":
        rads = math.radians(ship_heading)
        ship_x += math.cos(rads) * units
        ship_y += math.sin(rads) * units

print abs(ship_x) + abs(ship_y)
