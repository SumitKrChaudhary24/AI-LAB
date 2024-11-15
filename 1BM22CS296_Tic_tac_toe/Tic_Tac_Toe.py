def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board):
    """Checks for a winner or a draw."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check for draw
    for row in board:
        if " " in row:
            return None  # Game is still ongoing

    return "Draw"  # All cells are filled and no winner


def tic_tac_toe():
    """Main function to play the Tic Tac Toe game."""
    # Initialize an empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    current_player = "X"
    while True:
        print(f"Player {current_player}'s turn.")
        try:
            # Ask for the row and column
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))

            # Check if the cell is empty
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input! Row and column must be between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("Cell already occupied! Choose another cell.")
                continue

            # Make the move
            board[row][col] = current_player
            print_board(board)

            # Check for a winner
            result = check_winner(board)
            if result:
                if result == "Draw":
                    print("It's a draw!")
                else:
                    print(f"Player {result} wins!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Invalid input! Please enter numbers between 0 and 2.")
        except Exception as e:
            print(f"An error occurred: {e}")


# Run the game
tic_tac_toe()
