import itertools

consecutive_1_possiblities = {}
def possible_paths_through_n_consecutive_ones(n):
    if n in consecutive_1_possiblities.keys():
        return consecutive_1_possiblities[n]
    
    adapt_list = [3]
    for _ in range(n):
        adapt_list.append(adapt_list[-1] + 1)

    adapt_list.append(adapt_list[-1] + 3)
    #print adapt_list

    possibilities = 0
    for i in range(n):
        for c in itertools.combinations(adapt_list[1:n], i):
            t_list = adapt_list[:]
            valid = True        
            for el in c:
                t_list.remove(el)
            for i in range(len(t_list)-1):
                if t_list[i+1] - t_list[i] > 3:
                    valid = False
                    break
            if valid:
                possibilities += 1
    consecutive_1_possiblities[n] = possibilities
    return possibilities
        
print possible_paths_through_n_consecutive_ones(1)
print possible_paths_through_n_consecutive_ones(2)
print possible_paths_through_n_consecutive_ones(3)
print possible_paths_through_n_consecutive_ones(4)
print possible_paths_through_n_consecutive_ones(5)
print possible_paths_through_n_consecutive_ones(7)
print possible_paths_through_n_consecutive_ones(8)
print possible_paths_through_n_consecutive_ones(9)
print possible_paths_through_n_consecutive_ones(10)
print possible_paths_through_n_consecutive_ones(11)