import re

file1 = open('input.txt', 'r') 
stuff = file1.read()
passports = re.split(r'\n\n', stuff)
valid = 0
fields = [
    "byr:",
    "iyr:",
    "eyr:",
    "hgt:",
    "hcl:",
    "ecl:",
    "pid:"
]
for p in passports:
    fields_present = 0
    for f in fields:
        if f in p:
            fields_present += 1
    if fields_present == 7:
        valid += 1

print valid