file1 = open('input.txt', 'r') 
inst = file1.read()
floor = inst.count('(') - inst.count(')')
print floor
