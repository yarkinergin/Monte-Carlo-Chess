import random
import board
import pieces
import copy
whosMoveAI = "b"

def changeWhosMove(whosMove):
    if(whosMove == 'w'):
        return 'b'
    else:
        return 'w'

def evaluate_board(boardNew,whosMove):
    points = 0
    if(board.checkmate(boardNew, whosMoveAI)):
        points = 100
        return points
    if(board.checkmate(boardNew, whosMoveAI)):
        points = -100
        return points
    for row in boardNew:
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
    return points

def minimax(boardNew, depth, alpha, beta, maximizing_player, EnPassantAI,whosMove):
    boardOld = copy.deepcopy(boardNew)
    if depth == 0 or board.checkmate(boardNew, "b") or board.checkmate(boardNew, "w"):
        return None, evaluate_board(boardNew,whosMove)
    
    moves = board.find_moves(boardNew,whosMove,EnPassantAI)
    #bestMove = random.choice(moves)
    bestMove = moves[0]
    if maximizing_player:
        max_eval = float('-inf')
        for move in moves:
            boardNew = copy.deepcopy(boardOld)
            for moves2 in move:
                new_board, EnPassantAI = moveai(moves2, boardNew)
            whosMove = changeWhosMove(whosMove)
            evaluation = minimax(new_board, depth - 1, alpha, beta, False,EnPassantAI,whosMove)[1]
            if evaluation > max_eval:
                max_eval = evaluation
                bestMove = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return bestMove, max_eval
    else:
        min_eval = float('inf')
        for move in moves:
            boardNew = copy.deepcopy(boardOld)
            for moves2 in move:
                new_board, EnPassantAI = moveai(moves2, boardNew)
            whosMove = changeWhosMove(whosMove)
            evaluation = minimax(new_board, depth - 1, alpha, beta, True, EnPassantAI,whosMove)[1]
            if evaluation < min_eval:
                min_eval = evaluation
                bestMove = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return bestMove, min_eval

def ai(moves, chessBoard, EnPassant,whosMove):
    EnPassantAI = EnPassant
    alpha = float('-inf')
    beta = float('inf')
    bestMove, max = minimax(chessBoard, 5, alpha, beta, True, EnPassantAI,whosMove)
    print("max: ", max)
    return bestMove


def moveai(moves2, boardNew):
    new_board, EnPassantAI = board.make_move(boardNew[moves2[0][0]][moves2[0][1]],moves2[1],boardNew)
    return new_board, EnPassantAI