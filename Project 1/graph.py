from collections import defaultdict
from typing import Dict

class   Graph:

    def     __init__(self) :
        self.graph = defaultdict(list)
        self.heuristic= dict()

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def build(self, action): 

        file = open(action)
        for vertex in file: 
            vertex.strip("\n")
            if vertex != "END" : 
                node = vertex.split(" ")
                self.addEdge(node[0], [ node[1], int(node[2]) ] )
                self.addEdge(node[1], [ node[0], int(node[2]) ] )
        file.close()
    
    def successor(self, source) : 
        child = list()
        for node in self.graph : 
            if node == source :
                child = self.graph[node]
    
        return child

    def heuristic_func(self, input) : 
        file = open(input)

        for vertex in file:
            vertex = vertex.strip("\n")
            if (vertex != "") and ( vertex != "END" ) :
                state = vertex.split(" ")
                loc = state[0]
                h = int(state[-1])
                self.heuristic.update({loc: h})
        
        file.close()





###
# g = Graph()
#g.build("input_file1.txt")
#a = g.successor("Toledo")
#print(a)
###
