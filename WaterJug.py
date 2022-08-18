def move_gen(node):
    result = []
    x, y = node
    dx, dy = A - x, B - y
    if x < A:
        # fill in Jug A, if it's not full
        result.append((A, y))
    if y < B:
        # fill in Jug B, if it's not full
        result.append((x, B))
    if x > 0:
        # empty Jug A, if it's not empty
        result.append((0, y))
    if y > 0:
        # empty Jug B, if it's not empty
        result.append((x, 0))
    if x > 0 and x + y <= B:
        # if water in jug A can be poured in jug B without overflowing B, do that
        result.append((0, x + y))
    if x > 0 and x + y > B:
        # if water in jug A can't be poured in jug B without overflowing B, pour water from A until B is full. Some water will be left in jug A
        result.append((x - dy, B))
    if y > 0 and y + x <= A:
        # if water in jug B can be poured in jug A without overflowing A, do that
        result.append((x + y, 0))
    if y > 0 and y + x > A:
        # if water in jug B can't be poured in jug A without overflowing A, pour water from B until A is full. Some water will be left in jug B
        result.append((A, y - dx))

    return result


def remove_seen(children, open_list, closed_list):
    open_heads_list = [i[0] for i in open_list]
    closed_heads_list = [i[0] for i in closed_list]
    return [i for i in children if i not in open_heads_list + closed_heads_list]


def make_pairs(children_list, parent):
    return [(child, parent) for child in children_list]


def find_link(node, closed_list):
    return list(filter(lambda x: x[0] == node, closed_list))[0]


def reconstruct_path(nodepair, closed_list):
    node, parent = nodepair
    result = [node]
    while parent is not None:
        node, parent = find_link(parent, closed_list)
        result.append(node)
    result.reverse()
    return result

if __name__ == '__main__':
    A, B = 4, 3
    start = (0, 0)
    goal = (0, 2)
    open = [(start, None)]
    closed = []
    while open:
        nodepair = open.pop(0)
        node = nodepair[0]
        if node == goal:
            print("Goal state can be reached through path:\n", *reconstruct_path(nodepair, closed))
            
        else:
            closed = [nodepair] + closed
            children = move_gen(node)
            noLoops = remove_seen(children, open, closed)
            new = make_pairs(noLoops, node)
            open = new + open       