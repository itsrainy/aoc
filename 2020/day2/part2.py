

file1 = open('input.txt', 'r') 
lines = file1.readlines()

valid_count = 0
for line in lines:
    counts, letter, password = line.split(' ')
    idx_1, idx_2 = counts.split('-')
    letter = letter[0]
    first_matches = bool(password[int(idx_1)-1] == letter)
    second_matches = bool(password[int(idx_2)-1] == letter)
    if first_matches != second_matches:
        valid_count += 1
    
print valid_count