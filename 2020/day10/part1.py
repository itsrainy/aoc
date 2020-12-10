file1 = open('input.txt', 'r') 
code = [int(s.strip()) for s in file1.readlines()]
preamble = code[:25]
for i, val in enumerate(code):
    if i <= 24:
        continue
    is_sum = False
    for n1 in preamble:
        for n2 in preamble:
            if val == n1 + n2:
                is_sum = True
                break
        if is_sum:
            break
    if is_sum == False:
        print val
        break
    else:
        preamble.pop(0)
        preamble.append(val)