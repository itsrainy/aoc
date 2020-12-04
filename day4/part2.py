import re

file1 = open('input.txt', 'r') 
stuff = file1.read()
passports = re.split(r'\n\n', stuff)
valid = 0
for p in passports:
    m = re.search(r'byr:(?P<year>[12]\d\d\d)(\s|$)', p)
    if m is None:
        continue
    year = int(m.group('year'))
    if year < 1920 or year > 2002:
        continue
    
    m1 = re.search(r'iyr:(?P<year>20[12]\d)(\s|$)', p)
    if m1 is None:
        continue
    year = int(m1.group('year'))
    if year < 2010 or year > 2020:
        continue
    
    m1 = re.search(r'eyr:(?P<year>20[23]\d)(\s|$)', p)
    if m1 is None:
        continue
    year = int(m1.group('year'))
    if year < 2020 or year > 2030:
        continue
    
    m2 = re.search(r'hgt:(?P<hgt>\d\d\dcm|\d\din)(\s|$)', p)
    if m2 is None:
        continue
    hgt = m2.group('hgt')

    if hgt.endswith("cm"):
        if int(hgt[:3]) < 150 or int(hgt[:3]) > 193:
            continue
    if hgt.endswith("in"):
        if int(hgt[:2]) < 59 or int(hgt[:2]) > 76:
            continue
    
    m3 = re.search(r'hcl:(#[0-9a-f]{6})(\s|$)', p)
    if m3 is None:
        continue
    
    m4 = re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)', p)
    if m4 is None:
        continue
    
    m5 = re.search(r'pid:\d{9}(\s|$)', p)
    if m5 is None:
        continue
    # import pdb; pdb.set_trace()
    valid += 1

print valid