from sys import path
from graph import Graph

def bfs(input, start, end):

    g = Graph()
    g.build(input)
    queue = [] #list to maintain frontier
    visited = set()
    

    if start == end : 
        return start

    queue.append([start]) #adding initial start point for the algorithm
    visited.add(start) #adding start node to the visited set

    while queue : 
        curr_path = queue.pop(0) #current path taken
        node = curr_path[-1] #assigning the last element in queue to node to expand

       

        if node == end : #goal test

            return curr_path
        
        for x in g.successor(node) : #going over each child that has not been visited of the current node and adding them to the path
            if x[0] not in visited : 
                #print("current cost is : " + str(cost))
                new_path=list(curr_path)
                new_path.append(x[0])
                #print(cost_list)
                queue.append(new_path) #updating the old path with new path taken by algorithm
                visited.add(x[0])

def bfs1(input, start, end):

    g = Graph()
    g.build(input)
    queue = [] #list to maintain frontier
    visited = set()
    c = []
    c.append(0)

    if start == end : 
        return start

    queue.append([start]) #adding initial start point for the algorithm
    visited.add(start) #adding start node to the visited set

    while queue : 
        curr_path = queue.pop(0) #current path taken
        node = curr_path[-1] #assigning the last element in queue to node to expand
        
       

        if node == end : #goal test
            return curr_path,c 
            


        
        for x in g.successor(node) : #going over each child that has not been visited of the current node and adding them to the path
            if x[0] not in visited : 
                #print("current cost is : " + str(cost))
                new_path=list(curr_path)
                new_path.append(x[0])
                c.append(x[1])
                #print(cost_list)
                queue.append(new_path) #updating the old path with new path taken by algorithm
                visited.add(x[0])





print(bfs1("input_file1.txt","Detroit","Lincoln"))