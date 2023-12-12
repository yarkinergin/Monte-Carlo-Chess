import random
import board
import pieces
import copy
whosMove = "b"

def evaluate_board(boardNew):
    return 0

def minimax(boardNew, depth, alpha, beta, maximizing_player, EnPassantAI):
    boardOld = copy.deepcopy(boardNew)
    if depth == 0 or board.checkmate(boardNew, whosMove):
        return None, evaluate_board(boardNew)
    
    moves = board.find_moves(boardNew,whosMove,EnPassantAI)
    bestMove = random.choice(moves)
    
    if maximizing_player:
        max_eval = float('-inf')
        for move in moves:
            boardNew = copy.deepcopy(boardOld)
            for moves2 in move:
                new_board, EnPassantAI = moveai(moves2, boardNew)
            evaluation = minimax(new_board, depth - 1, alpha, beta, False,EnPassantAI)[1]
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
            evaluation = minimax(new_board, depth - 1, alpha, beta, True, EnPassantAI)[1]
            if evaluation < min_eval:
                min_eval = evaluation
                bestMove = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return bestMove, min_eval

def ai(moves, chessBoard, EnPassant):
    EnPassantAI = EnPassant
    alpha = float('-inf')
    beta = float('inf')
    return minimax(chessBoard, 6, alpha, beta, True, EnPassantAI)[0]


def moveai(moves2, boardNew):
    new_board, EnPassantAI = board.make_move(boardNew[moves2[0][0]][moves2[0][1]],moves2[1],boardNew)
    return new_board, EnPassantAI