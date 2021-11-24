from graph import Graph
import queue

def ucs(input, start, end):
    g = Graph()
    g.build(input)  #creating graph based on input file
    #path = list()
    visited = set() #maintaining a set of visited nodes
    q = queue.PriorityQueue()  #a priority queue containing the 
                               #cost of path to node
                               #the current node being added 
                               #and the path taken so far by the algorithm

    q.put((0,start, [start]))

    while not q.empty():    
        f,curr_node,path = q.get() #unpacking the tuples in the queue
        visited.add(curr_node)     #adding current node in iteration to visited set


        if curr_node == end : #goal test
            print("The path is : " + str(path))
            print("The cost is : " + str(f))
            break
        
        else : 
            for x in g.successor(curr_node): #going through children of current that have not been viisted 
                                             #yet and adding their respective path cost
                if x[0] not in visited : 
                    q.put((f+x[1], x[0], path + [x[0]]))
    
    pass

#ucs("input_file1.txt", "Detroit", "Indianapolis")