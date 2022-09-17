import numpy as np


def check_line(line):
    prod_line = np.prod(line)

    if prod_line == 8:
        return 2
    elif prod_line == 1:
        return 1
    else:
        return 0


def check_horizontal(board):
    result = [
        check_line(board[0, : ]),
        check_line(board[1, : ]),
        check_line(board[2, : ])]

    return max(result)


def check_vertical(board):
    result = [
        check_line(board[ : ,0]),
        check_line(board[ : ,1]),
        check_line(board[ : ,2])]

    return max(result)


def check_diagonal(board):
    result = [
        check_line(board.diagonal()),
        check_line(np.fliplr(board).diagonal())]

    return max(result)


def check_winner(board):
    result = [
        check_horizontal(board),
        check_vertical(board),
        check_diagonal(board)]

    return max(result)


def is_solved(board):
    board = np.array(board)
    winner = check_winner(board)

    if winner > 0:
        return winner
    elif 0 in board:
        return -1
    return 0
