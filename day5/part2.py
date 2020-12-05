import math

file1 = open('input.txt', 'r') 
seats = file1.readlines()
max_num = 0
seat_ids = []
for seat in seats:
    binary = seat[:7].replace('F', '0').replace('B', '1')
    row = int(binary, 2)
    binary = seat[7:].replace('L', '0').replace('R', '1')
    column = int(binary, 2)
    seat_id = (row * 8) + column
    seat_ids.append(seat_id)

for i in range(32, 848): # i know there's a better way to do this but i am tired
    if i not in seat_ids:
        print i
