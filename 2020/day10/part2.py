file1 = open('input.txt', 'r') 
jolts = [int(s.strip()) for s in file1.readlines()]
jolts.sort()

# A string of this many consecutive 1s leads to this many possible
# paths through that sub-sequence of adapters
# I don't know what these numbers are... 
consecutive_1_possiblities = {
    1 : 1,
    2: 2,
    3: 4,
    4 : 7,
    5: 13,
}
possiblities = 1
consecutive_ones = 0
diffs = [jolts[0]]
for i in range(len(jolts)-1):
    diffs.append(jolts[i+1] - jolts[i])

for d in diffs:
    if d == 1:
        consecutive_ones += 1
    elif d == 3 and consecutive_ones > 0:
        possiblities *= consecutive_1_possiblities[consecutive_ones]
        consecutive_ones = 0
if consecutive_ones > 0:
    possiblities *= consecutive_1_possiblities[consecutive_ones]

print possiblities
