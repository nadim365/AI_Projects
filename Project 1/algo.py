from queue import Queue
from graph import Graph

def bfs(input, start, end):
    g = Graph()
    g.build(input)
    Q = Queue(maxsize = 0)
    visited = set()
    path = list()

    if start == end : 
        return start

    Q.put(start)
    visited.add(start)
    
    
    while not(Q.empty()) : 
        path = Q.get()
        v = path[-1]
    
        if v == end :
           return path
        
        for x in g.successor(v) : 
            if x[0] not in visited: 
                new_path = list(path)
                visited.add(x[0])
                new_path.append(x[0])
                Q.put(new_path)




print(bfs('input_file1.txt', "Detroit", "Springfield"))