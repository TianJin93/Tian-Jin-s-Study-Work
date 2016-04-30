import Queue
import copy
import math

moves = [1, 3, -1, -3]
goal_state = [[[1, 2, 3, 4, 5, 6, 7, 8, ''], 8]]    # state -> [[[chess panel], position of space]]

#######################################################
def makeState(state):
    """
    echo the state
    :param state -> [[[chess panel], position of space]]
    :return:
    """
    print state[0][0][0:3]
    print state[0][0][3:6]
    print state[0][0][6:9]
#######################################################
def createState(*args):
    """
    state -> [[chess panel], position of blank]
    :param args: chess panel
    :return: state
    """
    lst = [x for x in args]
    pos = 0
    for i in range(len(lst)):
        if lst[i] is '':
            pos = i
            break
    return [lst, pos]
#######################################################
def makeNode(state, parent, depth=0, pathCost=0):
    """
    used to reconstruct the path
    :param state: state [[panel], space_position]
    :param parent:
    :param depth:
    :param pathCost:
    :return:
    """
    return [state, parent, depth, pathCost]
#######################################################
def expand(direcs, cur_state):
    if (direcs == 0 and cur_state[0][1] % 3 == 2) or \
        (direcs == 1 and cur_state[0][1] > 5) or \
        (direcs == 2 and cur_state[0][1] % 3 == 0) or \
            (direcs == 3 and cur_state[0][1] < 3):
        # do nothing
        return None
    else:
        # expand
        new_state = copy.deepcopy(cur_state)
        tmp = new_state[0][1]    # original blank position
        new_state[0][1] += moves[direcs]
        new_state[0][0][tmp] = new_state[0][0][new_state[0][1]]
        new_state[0][0][new_state[0][1]] = ''
        return new_state

#######################################################
def uninformed_search(start_state, limit, steps):
    """
    Breadth First search
    :param start_state:
    :param limit:
    :param steps:
    :return:
    """

    que = Queue.Queue()    # queue of nodes, node -> [state, parent, depth, pathCost]
    que.put(makeNode(start_state, -1, 0))    # put the first state start_state node
    lst = []    # list of nodes, node -> [state, parent, depth, pathCost]
    l = limit

    while que.empty() is False:

        cur_node = que.get()
        lst.append(cur_node)
        # is goal
        cur_state = cur_node[0]
        l -= 1

        if l < 0:
            print 'Limit reached'
            return False # stops after limit reached, prevents infinite looping

        if cur_state == goal_state:
            # print
            stack = []
            cur_n = lst[len(lst) - 1]
            while cur_n[1] != -1:
                stack.append(cur_n)
                cur_n = lst[cur_n[1]]
            stack.append(cur_n)

            for i in stack[len(stack) - 1::-1]:
                makeState(i[0])
                print("-----------")

            return

        # expand
        cur_fa = len(lst) - 1
        for direcs in range(4):    # 0 to right, 1 to down, 2 to left, 3 to up

            if (direcs == 0 and cur_state[0][1] % 3 == 2) or \
                    (direcs == 1 and cur_state[0][1] > 5) or \
                    (direcs == 2 and cur_state[0][1] % 3 == 0) or \
                    (direcs == 3 and cur_state[0][1] < 3):
                # do nothing
                pass
            else:
                # expand
                new_state = copy.deepcopy(cur_state)
                tmp = new_state[0][1]    # original blank position
                new_state[0][1] += moves[direcs]
                new_state[0][0][tmp] = new_state[0][0][new_state[0][1]]
                new_state[0][0][new_state[0][1]] = ''

                def is_visited(nodes):
                    return new_state == nodes[0]

                if len(list(filter(is_visited, lst))) == 0:    # is not visited
                    # create new node
                    que.put(makeNode(new_state, cur_fa, 0))
#######################################################
dfs_lst = []    # list of visited nodes
def dfs(new_state, term_state, fa_idx, limit, steps):
    """
    Depth First Search
    :param start_state:
    :param term_state:
    :param fa_idx:
    :param limit:
    :param steps:
    :return:
    """
    new_node = makeNode(new_state, fa_idx, 0)
    dfs_lst.append(new_node)

    if limit < 0:
        print 'Limit reached'
        return True # stops after limit reached, prevents infinite looping

    # is goal
    if new_state == term_state:
        # print
        stack = []
        cur_n = dfs_lst[len(dfs_lst) - 1]
        while cur_n[1] != -1:
            stack.append(cur_n)
            cur_n = dfs_lst[cur_n[1]]
        stack.append(cur_n)

        for i in stack[len(stack) - 1::-1]:
            makeState(i[0])
            print("-----------")

        return True

    # expand
    cur_fa_idx = len(dfs_lst) - 1
    for direcs in range(4):    # 0 to right, 1 to down, 2 to left, 3 to up

            if (direcs == 0 and new_state[1] % 3 == 2) or \
                    (direcs == 1 and new_state[1] > 5) or \
                    (direcs == 2 and new_state[1] % 3 == 0) or \
                    (direcs == 3 and new_state[1] < 3):
                # do nothing
                pass
            else:
                # expand
                new_state_next_iter = copy.deepcopy(new_state)
                tmp = new_state_next_iter[1]    # original blank position
                new_state_next_iter[1] += moves[direcs]
                new_state_next_iter[0][tmp] = new_state_next_iter[0][new_state_next_iter[1]]
                new_state_next_iter[0][new_state_next_iter[1]] = ''

                def is_visited(nodes):
                    return new_state_next_iter == nodes[0]

                if len(list(filter(is_visited, dfs_lst))) == 0:    # is not visited
                    # create new node
                    is_over = dfs(new_state_next_iter, term_state, cur_fa_idx, limit - 1, 0)
                    if is_over:
                        return True
                    else:
                        continue
    return False
#######################################################
def heuristic1(state, goal):
    sum = 0
    for i in range(len(goal[0][0])):
        for j in range(len(state[0][0])):
            if state[0][0][i] == goal[0][0][j]:
                x1 = i / 3
                y1 = i % 3
                x2 = j / 3
                y2 = j % 3
                sum += (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)

    return sum

def heuristic2(state, goal):
    """
    cosine similarity
    :param state:
    :param goal:
    :return:
    """
    sum = 0
    for i in range(len(goal[0][0])):
        for j in range(len(state[0][0])):
            if state[0][0][i] == goal[0][0][j]:
                x1 = i / 3 + 1
                y1 = i % 3 + 1
                x2 = j / 3 + 1
                y2 = j % 3 + 1
                at1 = math.atan2(y1, x1)
                at2 = math.atan2(y2, x2)
                sum += math.cos(math.fabs(at1 - at2))
    return 1 / sum

def informedSearch(start_state, limit, steps, heuristic_func):
    pass
    prior_queue = Queue.PriorityQueue()
    price = heuristic_func(start_state, goal_state)
    prior_queue.put((price, makeNode(start_state, -1, 0)))    # put the first state start_state node
    lst = []
    l = limit

    while prior_queue.empty() is False:
        cur_node = prior_queue.get()[1]
        lst.append(cur_node)
        cur_state = cur_node[0]
        l -= 1

        # limit
        if l < 0:
            print 'Limit reached'
            return False # stops after limit reached, prevents infinite looping

        # is goal
        if cur_state == goal_state:
            # print
            stack = []
            cur_n = lst[len(lst) - 1]
            while cur_n[1] != -1:
                stack.append(cur_n)
                cur_n = lst[cur_n[1]]
            stack.append(cur_n)

            for i in stack[len(stack) - 1::-1]:
                makeState(i[0])
                print("-----------")

            return
        # expand
        cur_fa = len(lst) - 1
        for direcs in range(4):    # 0 to right, 1 to down, 2 to left, 3 to up

            if (direcs == 0 and cur_state[0][1] % 3 == 2) or \
                    (direcs == 1 and cur_state[0][1] > 5) or \
                    (direcs == 2 and cur_state[0][1] % 3 == 0) or \
                    (direcs == 3 and cur_state[0][1] < 3):
                # do nothing
                pass
            else:
                new_state = copy.deepcopy(cur_state)
                tmp = new_state[0][1]    # original blank position
                new_state[0][1] += moves[direcs]
                new_state[0][0][tmp] = new_state[0][0][new_state[0][1]]
                new_state[0][0][new_state[0][1]] = ''

                def is_visited(node):
                    return new_state == node[0]

                if len(list(filter(is_visited, lst))) == 0:    # is not visited
                    # create new node
                    prior_queue.put((heuristic_func(new_state, goal_state), makeNode(new_state, cur_fa)))
#######################################################
def bidirectionalSearch(start_state, limit, steps):
    """
    Binary Breadth First Search
    :param start_state:
    :param limit:
    :param steps:
    :return:
    """
    pass
    que1 = Queue.Queue()
    que2 = Queue.Queue()
    que1.put(makeNode(start_state, -1, 0))    # put the first state start_state node
    que2.put(makeNode(goal_state, -1, 0))    # put the first state goal_state node
    lst1 = []
    lst2 = []
    # lst2.append(makeNode(goal_state, -1, 0))
    l = limit

    # begin looping
    while que1.empty() is False and que2.empty() is False:

        # whether searching start encounter searching goal
        cur_node_1 = que1.get()
        lst1.append(cur_node_1)
        cur_state_1 = cur_node_1[0]
        l -= 1

        if l < 0:
            print 'Limit reached'
            return False # stops after limit reached, prevents infinite looping

        def is_encounter(node):
            return cur_state_1 == node[0]
        if len(list(filter(is_encounter, lst2))) == 0:    # searching start NOT encounter searching goal
            cur_fa_1 = len(lst1) - 1
            for direcs in range(4):    # 0 to right, 1 to down, 2 to left, 3 to up
                new_state_1 = expand(direcs, cur_state_1)
                if new_state_1 is not None:
                    def is_visited(nodes):
                        return new_state_1 == nodes[0]
                    if len(list(filter(is_visited, lst1))) == 0:    # is not visited
                        # create new node
                        que1.put(makeNode(new_state_1, cur_fa_1, 0))


            # whether searching goal encounter searching start
            cur_node_2 = que2.get()
            lst2.append(cur_node_2)
            cur_state_2 = cur_node_2[0]
            l -= 1

            if l < 0:
                print 'Limit reached'
                return False # stops after limit reached, prevents infinite looping

            def is_encounter(node):
                return cur_state_2 == node[0]
            if len(list(filter(is_encounter, lst1))) == 0:    # searching goal NOT encounter searching start
                cur_fa_2 = len(lst2) - 1
                for direcs in range(4):    # 0 to right, 1 to down, 2 to left, 3 to up
                    new_state_2 = expand(direcs, cur_state_2)
                    if new_state_2 is not None:
                        def is_visited(nodes):
                            return new_state_2 == nodes[0]
                        if len(list(filter(is_visited, lst2))) == 0:    # is not visited
                            # create new node
                            que2.put(makeNode(new_state_2, cur_fa_2, 0))
            else: # searching goal encounter searching start
                idx_2 = 0
                for i in range(len(lst1)):
                    if cur_state_2 == lst1[i][0]:
                        idx_2 = i
                        break
                stack_2 = []
                cur_n_2 = lst1[idx_2]
                while cur_n_2[1] != -1:
                    stack_2.append(cur_n_2)
                    cur_n_2 = lst1[cur_n_2[1]]
                stack_2.append(cur_n_2)
                for i in stack_2[len(stack_2) - 1::-1]:
                    makeState(i[0])
                    print("-----------")

                cur_n_2 = lst2[lst2[len(lst2) - 1][1]]
                while cur_n_2[1] != -1:
                    makeState(cur_n_2[0])
                    cur_n_2 = lst2[cur_n_2[1]]
                    print("-----------")
                makeState(cur_n_2[0])

                return


        else:    # searching start encounter searching goal
            stack_1 = []
            cur_n_1 = lst1[len(lst1) - 1]
            while cur_n_1[1] != -1:
                stack_1.append(cur_n_1)
                cur_n_1 = lst1[cur_n_1[1]]
            stack_1.append(cur_n_1)
            for i in stack_1[len(stack_1) - 1::-1]:
                makeState(i[0])
                print("-----------")

            idx_1 = 0
            for i in range(len(lst2)):
                if cur_state_1 == lst2[i][0]:
                    idx_1 = i
                    break
            cur_n_1 = lst2[lst2[idx_1][1]]
            while cur_n_1[1] != -1:
                makeState(cur_n_1[0])
                cur_n_1 = lst2[cur_n_1[1]]
                print("-----------")
            makeState(cur_n_1[0])

            return




#######################################################
if __name__ == "__main__":
    pass
    # uninformed_search([createState('', 5, 2, 1, 4, 3, 7, 8, 6)],500,0)
    informedSearch([createState(3,2,1,4,5,6,7,8,'')], 1000000, 0, heuristic1)
    # bidirectionalSearch([createState('', 5, 2, 1, 4, 3, 7, 8, 6)], 2000, 0)