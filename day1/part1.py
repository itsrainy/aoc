

file1 = open('input.txt', 'r') 
lines = file1.readlines()

for i1 in lines:
    for i2 in lines:
        if int(i1) + int(i2) == 2020:
            print int(i1)*int(i2)