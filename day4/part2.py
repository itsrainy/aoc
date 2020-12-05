import re

file1 = open('input.txt', 'r') 
stuff = file1.read()
passports = re.split(r'\n\n', stuff)
valid = 0
regexes = [
    r'byr:(200[0-2]|19[2-9][0-9])(\s|$)',
    r'iyr:(20(1[0-9]|20))(\s|$)',
    r'eyr:(20(2[0-9]|30))(\s|$)',
    r'hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)(\s|$)',
    r'hcl:(#[0-9a-f]{6})(\s|$)',
    r'ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)',
    r'pid:\d{9}(\s|$)'
]
for p in passports:
    is_valid = True
    for r in regexes:
        if re.search(r, p) is None:
            is_valid = False
            break
    if is_valid:
        valid += 1

print valid