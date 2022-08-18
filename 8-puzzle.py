# -*- coding: utf-8 -*-
"""
@author: afaan

PROGRAM :- 8 PUZZLE
"""


def move_gen(node):
    result = []

    empty_pos = ()
    for i in range(3):
        for j in range(3):
            if node[i][j] == -1:
                empty_pos = (i, j)
                break
    
    neighbours = []
    for i in [1, -1]:
        neighbours.append((empty_pos[0]+i, empty_pos[1]))
        neighbours.append((empty_pos[0], empty_pos[1]+i))
    neighbours = list(filter(lambda x: 0 <= x[0] < 3 and 0 <= x[1] < 3, neighbours))

    for neighbour in neighbours:
        move = []
        for i in node:
            move.append(i[:])
        
        move[neighbour[0]][neighbour[1]], move[empty_pos[0]][empty_pos[1]] =move[empty_pos[0]][empty_pos[1]],move[neighbour[0]][neighbour[1]]
        result.append(move)

    return result


def remove_seen(children, open_list, closed_list):
    open_heads_list = [i[0] for i in open_list]
    closed_heads_list = [i[0] for i in closed_list]
    return [i for i in children if i not in (open_heads_list + closed_heads_list)]


def make_pairs(children_list, parent):
    return [(child, h(child), parent) for child in children_list]


def find_link(node, closed_list):
    return list(filter(lambda x: x[0] == node, closed_list))[0]


def reconstruct_path(nodepair, closed_list):
    node = nodepair[0]
    parent = nodepair[-1]
    result = [node]
    while parent is not None:
        node = find_link(parent, closed_list)[0]
        parent = find_link(parent, closed_list)[-1]
        result.append(node)
    result.reverse()
    return result


# state representation
# (x, y) ==> (amount of water in jug x, amount of water in jug y)
# (A, B) ==> max capacities of both the jugs
# (0, K) ==> goal state, where K represents the amount of water required, 0 < K < max(A, B)

def h(board):
    res = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == goal[i][j]:
                res += 1
    return res


if __name__ == '__main__':
    start = [
        [1,  2,  3],
        [7,  8,  4],
        [6, -1,  5]
    ]
    goal = [
        [1,  2,  3],
        [8, -1,  4],
        [7,  6,  5]
    ]

    solutionExists = False
    open = [(start, h(start), None)]
    closed = []
    while open:
        nodepair = open.pop(0)
        node = nodepair[0]
        if node == goal:
            print("Goal state can be reached through path:", *reconstruct_path(nodepair, closed))
            solutionExists = True
            break
            # break            
        else:
            closed = [nodepair] + closed
            children = move_gen(node)
            noLoops = remove_seen(children, open, closed)
            new = make_pairs(noLoops, node)
            open = sorted(new + open , key=lambda x:x[1], reverse=True)     # Best First Search
    if not solutionExists:
        print("No solution")
