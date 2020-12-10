import re

file1 = open('input.txt', 'r') 
bag_rules = file1.readlines()
def count_nested(color):
    count = 0
    for rule in bag_rules:
        if rule.startswith(color) and "no other bags" not in rule:
            nesteds = re.findall(r'\d+ \w+ \w+ bag', rule)
            for n in nesteds:
                num = int(n.split(' ')[0])
                c = ' '.join(n.split(' ')[1:3])
                count += (num + num*count_nested(c))
    return count

print count_nested('shiny gold')
