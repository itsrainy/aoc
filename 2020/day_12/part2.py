import math
file1 = open('input.txt', 'r') 
dirs = [s.strip() for s in file1.readlines()]

ship_x = 0.0
ship_y = 0.0
wp_x = 10.0
wp_y = 1.0

for d in dirs:
    direction = d[0]
    units = int(d[1:])
    if direction == "E":
        wp_x += units
    elif direction == "W":
        wp_x -= units
    elif direction == "N":
        wp_y += units
    elif direction == "S":
        wp_y -= units
    elif direction in ["L", "R"]:
        rads = math.radians(units)
        if direction == "R":
            rads *= -1.0
        new_x = math.cos(rads) * (wp_x - ship_x) - math.sin(rads) * (wp_y-ship_y) + ship_x
        new_y = math.sin(rads) * (wp_x - ship_x) + math.cos(rads) * (wp_y-ship_y) + ship_y
        wp_x = new_x
        wp_y = new_y
    elif direction == "F":
        add_x = (wp_x - ship_x) * units
        add_y = (wp_y - ship_y) * units
        ship_x += add_x
        ship_y += add_y
        wp_x += add_x
        wp_y += add_y

print abs(ship_x) + abs(ship_y)
