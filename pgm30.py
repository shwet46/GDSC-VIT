import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                empty_cells.append((row, col))
    return empty_cells

def ai_move(board):
    empty_cells = get_empty_cells(board)
    for row, col in empty_cells:
        board[row][col] = 'O'
        if check_win(board, 'O'):
            return (row, col)
        board[row][col] = ' '

    for row, col in empty_cells:
        board[row][col] = 'X'
        if check_win(board, 'X'):
            return (row, col)
        board[row][col] = ' '

    return random.choice(empty_cells)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True 

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for _ in range(9):
        if player_turn:
            row, col = map(int, input("Enter your move (row and column, e.g., 1 2): ").split())
            if board[row - 1][col - 1] != ' ':
                print("Invalid move. Try again.")
                continue
            board[row - 1][col - 1] = 'X'
        else:
            print("AI's turn:")
            row, col = ai_move(board)
            board[row][col] = 'O'

        print_board(board)

        if check_win(board, 'X'):
            print("Congratulations! You win!")
            break
        elif check_win(board, 'O'):
            print("AI wins! Better luck next time.")
            break

        player_turn = not player_turn
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
