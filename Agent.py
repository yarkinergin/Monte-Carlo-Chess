import random
import Node
import fen_setup
import ai
import board
import copy
import pieces

class Agent:
    def __init__(self, color):
        self.color = color

        exports = fen_setup.setup_fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
        chessBoard = exports[0]

        self.root = Node.Node(chessBoard, color, 0)

    def train(self, curNode, numIter):
        whosMove = self.color
        EnPassant = "-"

        """
        if (self.color == "b" and firtsTime):
            ai.firstBlackExpansion(curNode, EnPassant)
        """
        for i in range(numIter):
            curr_node = ai.selection(curNode, self.color, whosMove)

            legalMoves = board.find_moves(curr_node.chessBoard,self.color,EnPassant)

            curr_node = ai.expansion(curr_node, legalMoves, curr_node.chessBoard, EnPassant, self.color)

            if (curr_node != None):
                #print(board.print_board(curr_node.chessBoard))
                simBoard = copy.deepcopy(curr_node.chessBoard)
                reward = self.playChess(simBoard, whosMove, EnPassant)

                ai.backpropogation(curr_node, reward)

            whosMove = self.color

    def playChess(self, chessBoard, whosMove, EnPassant):
        stop = False
        move = False
        while not stop:
            #print(board.print_board(chessBoard))
            legalMoves = board.find_moves(chessBoard,whosMove,EnPassant)

            """
            points = 0
            for row in chessBoard:
                for piece in row:
                    if piece.colour == whosMove:
                        if isinstance(piece, pieces.Pawn):
                            points -= 1
                        if isinstance(piece, pieces.Rook):
                            points -= 5
                        if isinstance(piece, pieces.Knight) or isinstance(piece, pieces.Bishop):
                            points -= 3
                        if isinstance(piece, pieces.Queen):
                            points -= 9
                    if piece.colour != whosMove:
                        if isinstance(piece, pieces.Pawn):
                            points += 1
                        if isinstance(piece, pieces.Rook):
                            points += 5
                        if isinstance(piece, pieces.Knight) or isinstance(piece, pieces.Bishop):
                            points += 3
                        if isinstance(piece, pieces.Queen):
                            points += 9
                        
            print(points)
            """
            # Computer plays black
            """
            if whosMove == "b":
                move = ai.ai(legalMoves,chessBoard)
            else:
                while move == False:
                    move = board.convert_user_coords(input('>> '),chessBoard,whosMove,EnPassant)
                    if move not in legalMoves:
                        move = False
                    if move == False:
                        print("That's an illegal move. Try again.")
            """
            move = ai.ai(legalMoves,chessBoard)

            for moves in move:
                chessBoard, EnPassant = board.make_move(chessBoard[moves[0][0]][moves[0][1]],moves[1],chessBoard)
            move = False
            # if castling != '':
            #     castling = board.castling_rights(chessBoard,whosMove,castling)
            whosMove = "w" if whosMove == "b" else "b" # Swap
            if board.checkmate(chessBoard,whosMove) != False:
                #print(board.print_board(chessBoard))
                winLet = board.checkmate(chessBoard,whosMove) 
                if winLet == "w":
                    winner = 'White' 
                elif winLet == "b":
                    winner = 'Black'
                else:
                    winner = 'Draw!! No one'
                
                revcolor = "w" if self.color == "b" else "b" # Swap
                #print(f'{winner} has won the game!')
                stop = True
                if (winLet == self.color):
                    return 1
                elif (winLet == revcolor):
                    return -1
                else:
                    return 0
                
    def playHuman(self, numIter):
        exports = fen_setup.setup_fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
        chessBoard = exports[0]
        whosMove = exports[1]
        # castling = exports[2]
        EnPassant = exports[3]

        curNode =  self.root

        if (self.color == "b"):
            ai.firstBlackExpansion(curNode, EnPassant)

        stop = False
        move = False
        while not stop:
            print(board.print_board(chessBoard))
            legalMoves = board.find_moves(chessBoard,whosMove,EnPassant)

            """
            points = 0
            for row in chessBoard:
                for piece in row:
                    if piece.colour == whosMove:
                        if isinstance(piece, pieces.Pawn):
                            points -= 1
                        if isinstance(piece, pieces.Rook):
                            points -= 5
                        if isinstance(piece, pieces.Knight) or isinstance(piece, pieces.Bishop):
                            points -= 3
                        if isinstance(piece, pieces.Queen):
                            points -= 9
                    if piece.colour != whosMove:
                        if isinstance(piece, pieces.Pawn):
                            points += 1
                        if isinstance(piece, pieces.Rook):
                            points += 5
                        if isinstance(piece, pieces.Knight) or isinstance(piece, pieces.Bishop):
                            points += 3
                        if isinstance(piece, pieces.Queen):
                            points += 9
                        
            print(points)
            """

            # Computer plays black
            if whosMove == self.color:
                self.train(curNode, numIter)

                """
                for child in curNode.children:
                    print(child.data)
                """
                
                max_ucb = -100
                selected_child = None
                for i in curNode.children:
                    curr_ucb = i.data
                    if(curr_ucb > max_ucb):
                        max_ucb = curr_ucb
                        selected_child = i

                curNode = selected_child
                move = curNode.moveFrom

                #print("********")
                #print(curNode.data)

            else:
                """
                while move == False:
                    move = board.convert_user_coords(input('>> '),chessBoard,whosMove,EnPassant)
                    if move not in legalMoves:
                        move = False
                    if move == False:
                        print("That's an illegal move. Try again.")
                """
                move = ai.ai(legalMoves,chessBoard)
                
                for child in curNode.children:
                    if child.moveFrom == move:
                        curNode = child

            for moves in move:
                chessBoard, EnPassant = board.make_move(chessBoard[moves[0][0]][moves[0][1]],moves[1],chessBoard)
            move = False
            # if castling != '':
            #     castling = board.castling_rights(chessBoard,whosMove,castling)
            whosMove = "w" if whosMove == "b" else "b" # Swap
            if board.checkmate(chessBoard,whosMove) != False:
                print(board.print_board(chessBoard))
                winLet = board.checkmate(chessBoard,whosMove) 
                if winLet == "w":
                    winner = 'White' 
                elif winLet == "b":
                    winner = 'Black'
                else:
                    winner = 'Draw!! No one'
                
                print(f'{winner} has won the game!')
                stop = True
                if (winLet == "w"):
                    return 1
                elif (winLet == "b"):
                    return -1
                else:
                    return 0
                
    def showWay(self):
        curNode =  self.root
        whosMove = "w"        
        while curNode.children != []:
            print(board.print_board(curNode.chessBoard))
            print(whosMove)
            if(self.color == whosMove):
                max_ucb = -100
                selected_child = None
                for i in curNode.children:
                    curr_ucb = i.data
                    if(curr_ucb > max_ucb):
                        max_ucb = curr_ucb
                        selected_child = i
            else:
                min_ucb = 100
                selected_child = None
                for i in curNode.children:
                    curr_ucb = i.data
                    if(curr_ucb < min_ucb):
                        min_ucb = curr_ucb
                        selected_child = i

            curNode = selected_child

            whosMove = "w" if whosMove == "b" else "b" # Swap



    