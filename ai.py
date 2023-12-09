import random
import copy
from Node import Node
import board

def ai(moves,chessBoard):
    return random.choice(moves)

def agent(moves,chessboard):
    return random.choice(moves)
   
def selection(curr_node, playColor, whosMove):
    if(not curr_node.children):
        return curr_node
    
    if(playColor == whosMove):
        max_ucb = -100
        selected_child = None
        for i in curr_node.children:
            if i.checkmated == False:
                curr_ucb = i.data
                if(curr_ucb > max_ucb):
                    max_ucb = curr_ucb
                    selected_child = i
    else:
        min_ucb = 100
        selected_child = None
        for i in curr_node.children:
            if i.checkmated == False:
                curr_ucb = i.data
                if(curr_ucb < min_ucb):
                    min_ucb = curr_ucb
                    selected_child = i

    whosMove = "w" if whosMove == "b" else "b" # Swap
    
    return selection(selected_child, playColor, whosMove)

def expansion(curr_node, moves, chessBoard: list, EnPassant, whosMove):
    newNode = None
    newNode2 = None
    whosMoveReverse = "w" if whosMove == "b" else "b" # Swap
    for move in moves:
        newBoard = copy.deepcopy(chessBoard)

        for moves1 in move:
            newBoard, EnPassant = board.make_move(newBoard[moves1[0][0]][moves1[0][1]],moves1[1],newBoard)
        
        newNode = Node(newBoard, whosMoveReverse, move)
        curr_node.children.append(newNode)
        newNode.parent = curr_node

        winlet = board.checkmate(chessBoard,whosMove) != False
        if winlet != False:
            if winlet == whosMove:
                newNode.data = 1
            elif winlet == whosMoveReverse:
                newNode.data = -1
            else:
                newNode.data = 0
            
            newNode.checkmated = True

        legalMoves = board.find_moves(newBoard,whosMoveReverse,EnPassant)
        for move2 in legalMoves:
            newBoard2 = copy.deepcopy(newBoard)

            for moves1 in move2:
                newBoard2, EnPassant = board.make_move(newBoard2[moves1[0][0]][moves1[0][1]],moves1[1],newBoard2)
    
            newNode2 = Node(newBoard2, whosMove, move2)
            newNode.children.append(newNode2)
            newNode2.parent = newNode

            winlet = board.checkmate(chessBoard,whosMove) != False
            if winlet != False:
                if winlet == whosMove:
                    newNode2.data = 1
                elif winlet == whosMoveReverse:
                    newNode2.data = -1
                else:
                    newNode2.data = 0
                
                newNode2.checkmated = True

    return newNode2

def backpropogation(curr_node: Node, reward, playColor):
    addReward = reward
    while(curr_node != None):
        if(curr_node.whosMove == playColor):
            addReward = reward
        else:
            addReward = -reward

        curr_node.data = 4 * (curr_node.data / 5) + addReward / 5
        curr_node.sims += 1
        curr_node = curr_node.parent

    return curr_node