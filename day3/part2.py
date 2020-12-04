#!/usr/bin/python

file1 = open('input.txt', 'r') 
lines = file1.readlines()

tree_mult = 1
for slope in [[1,1], [3,1], [5,1], [7,1], [1,2]]:
    x_coord = slope[0]
    tree_count = 0
    for line in lines[slope[1]::slope[1]]:
        stripped = line.strip()
        line_len = len(stripped)
        if stripped[x_coord % line_len] == "#":
            tree_count += 1
        x_coord += slope[0]
    tree_mult *= tree_count
print tree_mult
