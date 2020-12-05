import math

file1 = open('input.txt', 'r') 
seats = file1.readlines()
max_num = 0
for seat in seats:
    binary = seat[:7].replace('F', '0').replace('B', '1')
    row = int(binary, 2)
    binary = seat[7:].replace('L', '0').replace('R', '1')
    column = int(binary, 2)
    seat_id = (row * 8) + column
    if seat_id > max_num:
        max_num = seat_id
print max_num