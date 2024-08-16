import random

ROWS = 6
COLS = 7
EMPTY = '🟢'
PLAYER1 = '🔴'
PLAYER2 = '🟡'
COLUMN_LABELS = "ABCDEFG"
DASH = '─'

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    # Print the top border
    print('  ' + ' '.join(DASH * 3 for _ in range(COLS)))
    
    # Print the board rows
    for row in reversed(board):
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        
        # Print the dashed line after each row
        print('  ' + ' '.join(DASH * 3 for _ in range(COLS)))
    
    # Print column labels
    print('  ' + ' '.join(f' {label} ' for label in COLUMN_LABELS))

def is_valid_location(board, col):
    return board[ROWS - 1][col] == EMPTY

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == EMPTY:
            return r

def winning_move(board, piece):
    # Check horizontal locations
    for r in range(ROWS):
        for c in range(COLS - 3):
            if (board[r][c] == piece and board[r][c + 1] == piece and 
                board[r][c + 2] == piece and board[r][c + 3] == piece):
                return True

    # Check vertical locations
    for c in range(COLS):
        for r in range(ROWS - 3):
            if (board[r][c] == piece and board[r + 1][c] == piece and 
                board[r + 2][c] == piece and board[r + 3][c] == piece):
                return True

    # Check positively sloped diagonals
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if (board[r][c] == piece and board[r + 1][c + 1] == piece and 
                board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece):
                return True

    # Check negatively sloped diagonals
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if (board[r][c] == piece and board[r - 1][c + 1] == piece and 
                board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece):
                return True

def get_random_move(board):
    valid_moves = [c for c in range(COLS) if is_valid_location(board, c)]
    return random.choice(valid_moves) if valid_moves else None

def column_to_index(col_str):
    """Convert column letter to index."""
    return COLUMN_LABELS.index(col_str.upper())

def index_to_column(index):
    """Convert index to column letter."""
    return COLUMN_LABELS[index]

def main():
    board = create_board()
    game_over = False
    turn = 0  # 0 for Player 1 (Human), 1 for Player 2 (AI)

    print_board(board)

    while not game_over:
        if turn == 0:
            # Player 1's turn (Human)
            col_str = input(f"Player 1 - Choose column ({COLUMN_LABELS}): ").upper()
            if col_str in COLUMN_LABELS:
                col = column_to_index(col_str)
            else:
                print("Invalid column. Try again.")
                continue
        else:
            # Player 2's turn (AI)
            col = get_random_move(board)
            col_str = index_to_column(col)
            print(f"Player 2 (AI) chooses column: {col_str}")

        if col is not None and is_valid_location(board, col):
            row = get_next_open_row(board, col)
            piece = PLAYER1 if turn == 0 else PLAYER2
            drop_piece(board, row, col, piece)

            if winning_move(board, piece):
                print_board(board)
                if turn == 0:
                    print("Player 1 wins!")
                else:
                    print("Player 2 (AI) wins!")
                game_over = True

            print_board(board)
            turn = (turn + 1) % 2  # Switch turn

        else:
            if turn == 0:
                print("Column full or invalid. Try again.")
            # AI doesn't need this check, it will always make a valid move

if __name__ == "__main__":
    main()
