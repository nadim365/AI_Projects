import sys
from threading import main_thread
import graph
import bfs
import dfs
import ucs
import astar



def main() : 
    if len(sys.argv) > 6 : 
     print("Pls enter the correct format : find_path.py [\"algorithm\"] [\"graph file\"] [\"start city\"] [\"end city]\" [\"**optional heuristic file\"]")
     return None
    algo = sys.argv[1]
    input = sys.argv[2]
    start = sys.argv[3]
    end  = sys.argv[4]
    
    if len(sys.argv) == 6 : 
        heuristic = sys.argv[5]

    if algo == "dfs" : 
        return print(dfs.dfs_5(input, start, end))
    elif algo == "bfs" : 
        return print(bfs.bfs(input, start, end))
    elif algo == "ucs" : 
        return ucs.ucs(input, start, end)
    elif algo == "astar" : 
        heuristic = sys.argv[5]
        return astar.astar2(input, start, end, heuristic)
    else : 
        print("choose the correct algorithm : dfs/bfs/ucs/astar")
        return None




if __name__ == "__main__" : 
        main() 



