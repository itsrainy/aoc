file1 = open('input.txt', 'r') 
inst = file1.read()
floor = 0
for i, c in enumerate(inst):
    if c == "(":
        floor += 1
    if c == ")":
        floor -= 1
    if floor < 0:
        print i+1
        break
