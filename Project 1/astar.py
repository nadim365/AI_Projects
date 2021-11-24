from typing import Dict
from graph import Graph
from queue import PriorityQueue
import queue

def astar (input, start, end, heuristic):
    g = Graph()
    g.build(input)
    g.heuristic_func(heuristic)
    h = g.heuristic
    G = {}
    F = dict(h)
    G[start] = 0 

    closed = set()
    open = set([start])
    came_from = {}

    while len(open) > 0 : 
        current = None
        curr_f = None
        for i in open : 
            if current is None or F[i] < curr_f : 
                curr_f = F[i]
                current = i

        if current == end : 
            path = [current]
            while current in came_from : 
                current = came_from[current]
                path.append(current) 

            path.reverse()
            return path, F[end]


        for x in g.successor(current) : 
            if x[0] in closed : 
                continue

            c_G = G[current] + x[1]

            if x[0] not in open : 
                open.add(x[0])
            elif c_G >= G[x[0]] : 
                continue

            came_from[x[0]] = current
            G[x[0]] = c_G
            H = h[x[0]]
            F[x[0]] = G[x[0]] + H

def astar1(input, start, end, heuristic) : 
    g = Graph()
    g.build(input)
    g.heuristic_func(heuristic)
    h = g.heuristic
    frontier =  PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    curr_cost = {}
    came_from[start] = None
    curr_cost[start] = 0

    while not frontier.empty() : 
        current = frontier.get()

        if current == end : 
            break
        
        for node in g.successor(current) : 
            new_cost = curr_cost[current] + node[1]
            

            if (node[0] not in curr_cost) or (new_cost < curr_cost[node[0]]) : 
                curr_cost[node[0]] = new_cost
                priority = new_cost + h[node[0]]
                frontier.put(node[0], priority)
                came_from[node[0]] = current
    
    return came_from, curr_cost

def astar2(input, start, end, heuristic): 
    #similar to UCS but the ordering is based on heuristic values instead of cost
    g = Graph()
    g.build(input)
    g.heuristic_func(heuristic)  #creating graph based on input file
    h = g.heuristic
    #path = list()
    visited = set() #maintaining a set of visited nodes
    q = queue.PriorityQueue()  #a priority queue containing the 
                               #cost of path to node
                               #the current node being added 
                               #and the path taken so far by the algorithm

    q.put((0,0,start, [start])) #initializing the queue

    while not q.empty():    
        o,f,curr_node,path = q.get() #unpacking the tuples in the queue
        visited.add(curr_node)     #adding current node in iteration to visited set


        if curr_node == end : #goal test
            print("The path is : " + str(path))
            print("The cost is : " + str(f))
            break
        
        else : 
            for x in g.successor(curr_node): #going through children of current that have not been viisted 
                                             #yet and adding their respective path cost
                if x[0] not in visited : 
                    q.put((h[x[0]] + x[1],f+x[1], x[0], path + [x[0]])) #pushing onto the queue along with their respective costs
    
    pass
 


#astar2("input_file1.txt", "Detroit", "Frankfort", "heuristic_Frankfort.txt") 
