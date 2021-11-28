# use math library if needed
import math
import random
from tkinter.constants import TRUE

def get_child_boards(player, board):
    """
    Generate a list of succesor boards obtained by placing a disc 
    at the given board for a given player
   
    Parameters
    ----------
    player: board.PLAYER1 or board.PLAYER2
        the player that will place a disc on the board
    board: the current board instance

    Returns
    -------
    a list of (col, new_board) tuples,
    where col is the column in which a new disc is placed (left column has a 0 index), 
    and new_board is the resulting board instance
    """
    res = []
    for c in range(board.cols):
        if board.placeable(c):
            tmp_board = board.clone()
            tmp_board.place(player, c)
            res.append((c, tmp_board))
    return res


def evaluate(player, board):
    """
    This is a function to evaluate the advantage of the specific player at the
    given game board.

    Parameters
    ----------
    player: board.PLAYER1 or board.PLAYER2
        the specific player
    board: the board instance

    Returns
    -------
    score: float
        a scalar to evaluate the advantage of the specific player at the given
        game board
    """
    adversary = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
    # Initialize the value of scores
    # [s0, s1, s2, s3, --s4--]
    # s0 for the case where all slots are empty in a 4-slot segment
    # s1 for the case where the player occupies one slot in a 4-slot line, the rest are empty
    # s2 for two slots occupied
    # s3 for three
    # s4 for four
    score = [0]*5
    adv_score = [0]*5

    # Initialize the weights
    # [w0, w1, w2, w3, --w4--]
    # w0 for s0, w1 for s1, w2 for s2, w3 for s3
    # w4 for s4
    weights = [0, 1, 4, 16, 1000]

    # Obtain all 4-slot segments on the board
    seg = []
    invalid_slot = -1
    left_revolved = [
        [invalid_slot]*r + board.row(r) + \
        [invalid_slot]*(board.rows-1-r) for r in range(board.rows)
    ]
    right_revolved = [
        [invalid_slot]*(board.rows-1-r) + board.row(r) + \
        [invalid_slot]*r for r in range(board.rows)
    ]
    for r in range(board.rows):
        # row
        row = board.row(r) 
        for c in range(board.cols-3):
            seg.append(row[c:c+4])
    for c in range(board.cols):
        # col
        col = board.col(c) 
        for r in range(board.rows-3):
            seg.append(col[r:r+4])
    for c in zip(*left_revolved):
        # slash
        for r in range(board.rows-3):
            seg.append(c[r:r+4])
    for c in zip(*right_revolved): 
        # backslash
        for r in range(board.rows-3):
            seg.append(c[r:r+4])
    # compute score
    for s in seg:
        if invalid_slot in s:
            continue
        if adversary not in s:
            score[s.count(player)] += 1
        if player not in s:
            adv_score[s.count(adversary)] += 1
    reward = sum([s*w for s, w in zip(score, weights)])
    penalty = sum([s*w for s, w in zip(adv_score, weights)])
    return reward - penalty


def minimax(player, board, depth_limit):
    """
    Minimax algorithm with limited search depth.

    Parameters
    ----------
    player: board.PLAYER1 or board.PLAYER2
        the player that needs to take an action (place a disc in the game)
    board: the current game board instance
    depth_limit: int
        the tree depth that the search algorithm needs to go further before stopping
    max_player: boolean

    Returns
    -------
    placement: int or None
        the column in which a disc should be placed for the specific player
        (counted from the most left as 0)
        None to give up the game
    """
    max_player = player
    placement = None

### Please finish the code below ##############################################
###############################################################################
    #next_player = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
    #MAX_p = True
    def value(player, board, depth_limit):
        #print(board)
        #base case : checks if the game is over or depth limit is reached ->outputs winner
        if board.terminal() or depth_limit == 0 :
            #evaluating from MAX player POV at terminal nodes
            return [evaluate(max_player, board),0]
        
        #if player is max player -> return max value of that state
        if(max_player == player):
            return max_value(player, board, depth_limit)

        #if player is min player -> return min value of that state
        else:
            return min_value(player, board, depth_limit)

    def max_value(player, board, depth_limit):
        #function to return max value of a state (state is current instance of game board)
        print("max_value")
        #intialize max value to be -infinity
        v = -math.inf
        max_v = -math.inf
        col_num = 0
        #gets the list of successor states at that depth
        for c,b in get_child_boards(player, board):
            v = value(next_player, b, depth_limit-1)[0]
            if(max_v < v):
                max_v = v
                col_num = c
        
        print("max-score = " + str(max_v))
        return max_v, col_num
    
    def min_value(player, board, depth_limit):
        print("min_value")
        v = math.inf
        min_v = math.inf
        col_num = 0
        
        for c,b in get_child_boards(player, board):
            v = value(next_player, b, depth_limit-1)[0]
            if(min_v > v):
                min_v = v
                col_num = c
        
        print("min-score = " + str(min_v))
        return min_v,col_num

    
    next_player = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
    placement = value(player, board,depth_limit)[1]
    score = -math.inf

###############################################################################
    return placement


def alphabeta(player, board, depth_limit):
    """
    Minimax algorithm with alpha-beta pruning.

     Parameters
    ----------
    player: board.PLAYER1 or board.PLAYER2
        the player that needs to take an action (place a disc in the game)
    board: the current game board instance
    depth_limit: int
        the tree depth that the search algorithm needs to go further before stopping
    alpha: float
    beta: float
    max_player: boolean


    Returns
    -------
    placement: int or None
        the column in which a disc should be placed for the specific player
        (counted from the most left as 0)
        None to give up the game
    """
    max_player = player
    placement = None

### Please finish the code below ##############################################
###############################################################################
    def value(player, board, depth_limit, alpha, beta):
        #if we reach terminal node for that depth or depth limit is reached -> return score
        if board.terminal() or depth_limit == 0 :
            #evaluating from MAX player POV at terminal nodes
            return [evaluate(max_player, board),0]
        #if player is max player -> return max value of that state
        if(max_player == player):
            return max_value(player, board, depth_limit, alpha, beta)
        #else if player is min player -> return min value of that state
        else:
            return min_value(player, board, depth_limit, alpha, beta)
    

    def max_value(player, board, depth_limit, alpha, beta):
        v = -math.inf
        max_v = -math.inf
        beta = +math.inf
        col_num = 0
        #iterating over the successors of the current game board
        for c,b in get_child_boards(player, board):
            v = value(next_player, b, depth_limit-1, alpha, beta)[0]
            #finds column associated with max value
            if(v >= max_v):
                max_v = v
                col_num = c
            alpha = max(alpha, max_v)
            #prune the tree if estimate(alpha) is greater than beta
            if(alpha > beta):
                break
         
        return max_v, col_num
       

    
    def min_value(player, board, depth_limit, alpha, beta):
        v = math.inf
        min_v = math.inf
        alpha = -math.inf
        col_num = 0
        #iterating over the successors of the current game board
        for c,b in get_child_boards(player, board):
            v = value(next_player, b, depth_limit-1, alpha, beta)[0]
            #finds column associated with min value
            if(v <= min_v):
                min_v = v
                col_num = c
            beta = min(beta, min_v)
            #prune the tree if estimate(beta) is less than alpha
            if(alpha > beta):
                break
                
        return min_v,col_num 
    
    next_player = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
    alpha = -math.inf
    beta = math.inf
    placement = value(player, board,depth_limit, alpha, beta)[1]
    score = -math.inf
###############################################################################
    return placement


def expectimax(player, board, depth_limit):
    """
    Expectimax algorithm.
    We assume that the adversary of the initial player chooses actions
    uniformly at random.
    Say that it is the turn for Player 1 when the function is called initially,
    then, during search, Player 2 is assumed to pick actions uniformly at
    random.

    Parameters
    ----------
    player: board.PLAYER1 or board.PLAYER2
        the player that needs to take an action (place a disc in the game)
    board: the current game board instance
    depth_limit: int
        the tree depth that the search algorithm needs to go before stopping
    max_player: boolean

    Returns
    -------
    placement: int or None
        the column in which a disc should be placed for the specific player
        (counted from the most left as 0)
        None to give up the game
    """
    max_player = player
    placement = None
 

### Please finish the code below ##############################################
###############################################################################

    def value(player, board, depth_limit):
        #if we reach terminal node for that depth or depth limit is reached -> return score
        if board.terminal() or depth_limit == 0 :
            #evaluating from MAX player POV at terminal nodes
            return [evaluate(max_player, board),0]
        #if player is max player -> return max value of that state
        if(max_player == player):
            return max_value(player, board, depth_limit)
        #else if player is min player -> return min value of that state
        else:
            return exp_value(player, board, depth_limit)

    def max_value(player, board, depth_limit):
        v = -math.inf
        max_value = -math.inf
        col_num = 0
        #iterating over the successors of the current game board
        for c,b in get_child_boards(player, board):
            v = value(next_player, b, depth_limit-1)[0]
            #finds column associated with max value
            if(max_value < v):
                max_value = v
                col_num = c

        
        return max_value, col_num   
    
    def exp_value(player, board, depth_limit):
        v = 0
        exp_val = 0
        #iterating over the successors of the current game board
        for c,b in get_child_boards(player, board):
            #all children have equal probability of being picked -> probability = 1/n [n = number of children]
            p = 1/len(get_child_boards(next_player, b))
            #averaging step
            v = v + p*value(next_player, b, depth_limit-1)[0]
            if(exp_val < v):
                exp_val = v
        
        return exp_val, None

    next_player = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
    placement = value(player, board,depth_limit)[1]
    score = -math.inf
###############################################################################
    return placement


if __name__ == "__main__":
    from game_gui import GUI
    import tkinter

    algs = {
        "Minimax": minimax,
        "Alpha-beta pruning": alphabeta,
        "Expectimax": expectimax
    }
    
    root = tkinter.Tk()
    GUI(algs, root)
    root.mainloop()
