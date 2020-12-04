

file1 = open('input.txt', 'r') 
lines = file1.readlines()

tree_count = 0
x_coord = 3
for line in lines[1:]:
    stripped = line.strip()
    line_len = len(stripped)
    if stripped[x_coord % line_len] == "#":
        tree_count += 1
    x_coord += 3
    
print tree_count
