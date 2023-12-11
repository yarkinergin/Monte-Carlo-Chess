import fen_setup
import board
import ai
import pieces
import copy
import random
import Agent
from Node import Node

# Start setup is 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

            
# Monte Carlo
agentWhite = Agent.Agent("b")
print("------------------")
agentWhite.playHuman(100)
"""
exports = fen_setup.setup_fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
chessBoard = exports[0]
whosMove = exports[1]
# castling = exports[2]
EnPassant = exports[3]

root = Node(chessBoard, "w", 0)

for i in range(10):
    curr_node = ai.selection(root, "w", whosMove)

    legalMoves = board.find_moves(curr_node.chessBoard,whosMove,EnPassant)

    print(random.choice(legalMoves))
    print(board.print_board(root.chessBoard))
    
    curr_node = ai.expansion(curr_node, legalMoves, curr_node.chessBoard, EnPassant, whosMove)

    simBoard = copy.deepcopy(curr_node.chessBoard)
    reward = playChess(simBoard, whosMove, EnPassant)

    ai.backpropogation(curr_node, reward, "w")

    exports = fen_setup.setup_fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
    chessBoard = exports[0]
    whosMove = exports[1]
    # castling = exports[2]
    EnPassant = exports[3]
"""