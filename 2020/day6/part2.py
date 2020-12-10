import re

file1 = open('input.txt', 'r') 
stuff = file1.read()
group = re.split(r'\n\n', stuff)
total_count = 0
for g in group:
    people = g.split('\n')
    group_set = set(people[0])
    for p in people[1:]:
        group_set = group_set.intersection(set(p))

    total_count += len(group_set)

print total_count