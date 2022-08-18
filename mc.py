# EXP 1: Missionaries and cannibals
# Taking value of boat on left side as B=0 && value of boat on right side as B=1
# checking the state

# (M, C, B, []) 
# M - miss on left side
# C - cann on left side
# B - 0 (left) or 1 (right)
# []

solutions = []

def is_valid(state):
    # 0 - M
    # 1 - C
    # 2 - B
    if(state[0]>3 or state[1]>3  or state[1]<0 or state[0]<0 or (state[0] !=0 and state[0]<state[1])  or (3-state[0] != 0 and 3-state[0]<(3-state[1]))):
        return False
    else:
        return True


# updating the state
def next_state(M,C,B):
    moves = [[1, 1],[1, 0],[0, 1],[0, 2],[2, 0]]
    valid_states = []
    for each in moves:
        if(B==1):
            next_state = [M+each[0], C+each[1], 0]
            # # [M+1, C+0, 0]
            # # [3, 3, 0], [0, 2]
            # # [3, 1, 1]
        else:
            next_state = [M-each[0], C-each[1], 1]
            # next_state.append(1)

        if (is_valid(next_state)):
            valid_states.append(next_state)
    return valid_states


def find_solution(M,C,B,path_visited):
    if([M,C,B]==[0,0,1]):
        
        solutions.append(path_visited+[[0,0,1]])        # another solution found, append to solutions array. [ [[3, 3, 0], [2, 2, 1]..., [0, 0, 1]], [[]] ] 
        return True

    elif([M,C,B] in path_visited):
        return False
    else:
        path_visited.append([M,C,B])
        for current_state in next_state(M,C,B):
            find_solution(current_state[0],current_state[1],current_state[2],path_visited[:])
        # input: [3, 3, 0]  ------>  [[1, 3, 1] X, [3, 1, 1], [2, 2, 1], [2, 3, 1] X, [3, 2, 1]]
        # at any time, missionaries should be >= cannibals on the left bank

find_solution(3,3,0,[])

# solutions.sort()
for soln in solutions:
    print('\n', soln,'\n \n SOLUTION FOUND')
