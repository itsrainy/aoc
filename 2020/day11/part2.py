import itertools, copy
file1 = open('input.txt', 'r') 
life_board = [list(s.strip()) for s in file1.readlines()]
next_board = copy.deepcopy(life_board)
adj = list(itertools.product([0, 1, -1], repeat=2))
adj.remove((0,0))

def compare_boards(b1, b2):
    for i in range(len(b1)):
        for j in range(len(b1[0])):
            if b1[i][j] != b2[i][j]:
                return False
    import pdb; pdb.set_trace()
    return True

def count_occupied(b):
    occ = 0
    for r in b:
        for c in r:
            if c == "#":
                occ += 1
    return occ

def count_adj_occupied(b, idx):
    adj_full = 0
    for a in adj:
        check_i = idx[0] + a[0]
        check_j = idx[1] + a[1]
        while check_i < len(life_board) and check_j < len(life_board[0]) and check_i >= 0 and check_j >= 0:
            cell = life_board[check_i][check_j]
            if cell != '.':
                if cell == "#":
                    adj_full += 1
                break
            else:
                check_i += a[0]
                check_j += a[1]
    return adj_full

while True:
    changed = False
    for i in range(len(life_board)):
        for j in range(len(life_board[0])):
            adj_full = count_adj_occupied(life_board, (i, j))
            if life_board[i][j] == "L" and adj_full == 0:
                changed = True
                next_board[i][j] = "#"
            elif life_board[i][j] == "#" and adj_full >= 5:
                changed = True
                next_board[i][j] = "L"
    if not changed:
        break
    life_board = copy.deepcopy(next_board)

print count_occupied(life_board)
