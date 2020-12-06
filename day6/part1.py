import re

file1 = open('input.txt', 'r') 
stuff = file1.read()
group = re.split(r'\n\n', stuff)
total_count = 0
for g in group:
    total_count += len(set(g.replace('\n', '')))

print total_count