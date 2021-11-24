from queue import Queue
from sys import path
from graph import Graph

def dfs(input, start, end) : 
    g = Graph()
    g.build(input)
    visited = list()
    visited.append([start])
    if start == end : 
        return visited
    for x in g.successor(start) : 
        if x[0] not in visited : 
            visited.append(x[0])
            dfs(input, x[0], end)

def dfs_1(input, start, end) : 
    g=Graph()
    g.build(input)
    visited = list()

    if start == end : 
        return start
    else:
        solution = recursive_dfs(g, start, end, visited)

    return solution

def recursive_dfs(graph, node, end, visited):
    if node not in visited : 
        visited.append(node)

        for x in graph.successor(node):
            if x[0] == end : 
                return visited
            recursive_dfs(graph, x[0], end, visited)

    return visited


def dfs_2 (input, start, end) : 
    g = Graph()
    g.build(input)
    stack = list()
    visited = list()
    #visited.append([start])
    stack.append((start, [start]))

    while stack : 
        (v, path) = stack.pop()
        if v not in visited : 
            if v == end : 
                return path
            visited.append(v)

        for x in g.successor(v):
            stack.append((x[0], path + [x[0]]))


def dfs_3 (input, start, end):
    g = Graph() 
    visited = list()
    g.build(input)
    queue = []
    queue.append([start])
    #visited.append(start)
    


    if start == end: 
        return start
    
    while queue:
        path = queue.pop()
        node = path[-1]

        if node not in visited : 
            if node == end:
                return path
            
            visited.append(node)
            for x in g.successor(node):
                new_path = list(path)
                new_path.append(x[0])
                queue.append(new_path)


def dfs_4(input, start, end) : 
    g=Graph()
    g.build(input)
    visited = list()
    queue = []

    if start == end : 
        return start
    else:
        queue.append([start])
        solution = recursive_dfs(g, start, end, visited,queue)

    return solution

def recursive_dfs(graph, node, end, visited,queue):
    path = queue.pop()
    v = path[-1]

    if v not in visited : 
        visited.append(v)

        for x in graph.successor(v):
            if x[0] == end : 
                return path
            
            new_path = list(path)
            new_path.append(x[0])
            queue.append(new_path)
            recursive_dfs(graph, x[0], end, visited, queue)
    return path



def dfs_5(input, start, end):
    g = Graph()
    g.build(input)
    visited = list()
    queue = [] #initializing queue
    cost = [] #recording costs
    cost.append(0)
    if start == end : 
        return start
    else:
        #queue.append([start])
        queue.append(start)#adding start node
        if recursive_dfs2(g, start, end, visited,queue, cost): 
            sol = 0
            for i in cost : 
                sol = sol + int(i)# summing up costs
            print("the path taken is :" + str(queue))
            print("the cost of the edges to the goal is :" + str(sol))
            return None


def recursive_dfs1(graph, node, end, visited,queue):
    #path = queue.pop()
    v = node

    if v not in visited : 
        visited.append(v)

        for x in graph.successor(v):
            queue.append(x[0])

            if x[0] == end : 
                return True
            if recursive_dfs1(graph, x[0], end, visited, queue) == True : 
                return True
            else: 
                queue.pop()

    return False

def recursive_dfs2(graph, node, end, visited, queue, cost) : 
    v = node

    if v not in visited : #checks if node is in visited list
        visited.append(v) #adds it 

        for x in graph.successor(v):#going over every child
            queue.append(x[0])
            cost.append(x[1])

            if x[0] == end : 
                return True
            if recursive_dfs2(graph, x[0], end, visited, queue, cost) == True : 
                return True
            else: 
                cost.pop() #if it backtracks pop the cost and the node from the path
                queue.pop()

    return False


print(dfs_5("input_file1.txt", "Detroit", "Topeka"))
#print(dfs("inputfile1.txt", "Detroit", "Lincoln"))