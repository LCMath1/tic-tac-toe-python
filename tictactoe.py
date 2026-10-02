def print_board(board):
    # Go through each row of the board
    for row in board:
        displayRow = ""

        # Add each square to the row we are displaying
        for column in row:
            displayRow += str(column) + " "

        # Print the completed row
        print(displayRow)


def make_move(board, player):
    # Ask the player which column and row they want
    column = int(input("Which column would you like to play in? (1-3) ")) - 1
    row = int(input("Which row would you like to play in? (1-3) ")) - 1

    # If they do not enter a number between 1 and 3, let them try again
    if column < 0 or column > 2 or row < 0 or row > 2:
        print("Choose only between 1 and 3! Try again.")
        return make_move(board, player)

    # Check if the selected square is empty
    elif board[row][column] == "_":
        board[row][column] = player
    
    else:
        # Tell the player they cannot use that square and let them try again
        print("That square is already occupied! Try again.")
        return make_move(board, player)


def check_winner(board, player):
    # Check each row
    for row in board:
        if row == [player, player, player]:
            return True

    # Check the first column
    if board[0][0] == board[1][0] == board[2][0] == player:
        return True

    # Check the second column
    if board[0][1] == board[1][1] == board[2][1] == player:
        return True

    # Check the third column
    if board[0][2] == board[1][2] == board[2][2] == player:
        return True

    # Check the top-left to bottom-right diagonal
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    # Check the top-right to bottom-left diagonal
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    # No winning combination was found
    return False


def check_draw(board):
    # Keep track of how many squares are occupied
    count = 0

    # Go through every square on the board
    for row in board:
        for column in row:
            if column != "_":
                count += 1

    # If all 9 squares are occupied, the game is a draw
    if count == 9:
        return True

    return False


def turn(board, player):
    # Let the player make their move
    make_move(board, player)

    # Display the board after the move
    print_board(board)


def main():
    # Create an empty 3x3 board
    board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]

    # Display the starting board
    print_board(board)

    # Welcome the players
    print("Welcome to Tic-Tac-Toe!")

    # Ask which player goes first
    starter = input("Who will start: X or O? ")

    # Continue playing while there is no winner and no draw
    while not check_winner(board, starter) and not check_draw(board):
        print(f"{starter}'s turn:")

        # Let the current player make a move
        turn(board, starter)

        # Switch to the other player
        if starter == "X":
            starter = "O"
        else:
            starter = "X"


# Start the game
main()