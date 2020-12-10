import re

file1 = open('input.txt', 'r') 
bag_rules = file1.readlines()
total_count = 0
list_bags = set()
for br in bag_rules:
    if re.search(r'\d shiny gold bag', br) is not None:
        #import pdb; pdb.set_trace()
        list_bags.add(' '.join(br.split(' ')[:2]))

bag_len = len(list_bags)
while True:
    new_list_bags = set()
    for bag in list_bags:
        for rule in bag_rules:
            if re.search('\d ' + bag, rule) is not None:
                new_list_bags.add(' '.join(rule.split(' ')[:2]))
    list_bags = list_bags | new_list_bags
    if bag_len == len(list_bags):
        break
    bag_len = len(list_bags)

print list_bags
print bag_len