file1 = open('input.txt', 'r') 
code = file1.readlines()
swap_candidates = [i for i, inst in enumerate(code) if inst.startswith('jmp') or inst.startswith('nop')]
accum = 0
for inst in swap_candidates:
    visited_line = []
    exec_pointer = 0
    accum = 0
    while exec_pointer not in visited_line and exec_pointer < len(code):
        visited_line.append(exec_pointer)
        line = code[exec_pointer]
        if exec_pointer == inst:
            line = line.replace('nop', 'TEMP').replace('jmp', 'nop').replace('TEMP', 'jmp')
        if line.startswith('nop'):
            exec_pointer += 1
        elif line.startswith('acc'):
            accum += int(line.split(' ')[-1].strip())
            exec_pointer += 1
        elif line.startswith('jmp'):
            exec_pointer += int(line.split(' ')[-1].strip())
    if exec_pointer not in visited_line:
        break
        
print accum