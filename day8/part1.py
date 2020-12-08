file1 = open('input.txt', 'r') 
code = file1.readlines()
visited_line = []
exec_pointer = 0
accum = 0
while exec_pointer not in visited_line:
    visited_line.append(exec_pointer)
    line = code[exec_pointer]
    if line.startswith('nop'):
        exec_pointer += 1
    elif line.startswith('acc'):
        accum += int(line.split(' ')[-1].strip())
        exec_pointer += 1
    elif line.startswith('jmp'):
        exec_pointer += int(line.split(' ')[-1].strip())
        
print accum