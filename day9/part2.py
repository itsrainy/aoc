file1 = open('input.txt', 'r') 
code = [int(s.strip()) for s in file1.readlines()]
lidx = 0
ridx = 1
amble = code[:ridx]
target = 10884537
while sum(amble) != target:
    if sum(amble) < target:
        ridx += 1
    elif sum(amble) > target:
        lidx += 1
    amble = code[lidx:ridx]
print min(amble) + max(amble)
print sum(amble)