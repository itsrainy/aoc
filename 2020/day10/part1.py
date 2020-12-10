file1 = open('input.txt', 'r') 
jolts = [int(s.strip()) for s in file1.readlines()]
jolts.sort()
print jolts

one_diff_count = 0
three_count = 1
if jolts[0] == 1:
    one_diff_count += 1
elif jolts[0] == 3:
    three_count += 1
for i in range(len(jolts)-1):
    diff = jolts[i+1] - jolts[i]
    if diff == 1:
        one_diff_count += 1
    elif diff == 3:
        three_count += 1

print one_diff_count
print three_count
print one_diff_count * three_count