

file1 = open('input.txt', 'r') 
lines = file1.readlines()

valid_count = 0
for line in lines:
    counts, letter, password = line.split(' ')
    min_count, max_count = counts.split('-')
    letter = letter[0]
    letter_count = password.count(letter)
    if letter_count >= int(min_count) and letter_count <= int(max_count):
        valid_count += 1
    
print valid_count