from game import *

def play_game(start_player=X):
    board = initial_state()
    print("Game Start! Initial Board:")
    for row in board:
        print(row)

    current_player = start_player
    while not terminal(board):
        print(f"\nCurrent player: {current_player}")
        print("Available moves:", actions(board))
        
        if current_player == X:
            action = tuple(map(int, input("Enter your move as 'row col': ").split()))
            if action not in actions(board):
                print("Invalid move, try again.")
                continue
        else:
            action = minimax(board) # you can use alpha-beta algorithm
            print(f"Player {current_player} (Computer) chooses: {action}")
        
        board = result(board, action)
        for row in board:
            print(row)
        current_player = O if current_player == X else X

    print("\nGame Over!")
    if winner(board):
        print(f"The winner is: {winner(board)}")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game(start_player=X)
