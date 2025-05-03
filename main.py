import random
import time

    # Initialize the game board
board = [" " for _ in range(9)]

    # Function to print the current board state
def print_board():
        print()
        for i in range(3):
            print(" | ".join(board[i * 3:(i + 1) * 3]))
            if i < 2:
                print("--+---+--")
        print()

    # Check if a player has won
def is_winner(player):
        win_conditions = [
             [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
             [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
             [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(all(board[i] == player for i in condition) for condition in win_conditions)

    # Check if the game is a draw
def is_draw():
        return all(cell != " " for cell in board)

    # Player's move
def player_move():
        while True:
            try:
                move = int(input("\nChoose a position (1-9) to place 'X': ")) - 1
                if board[move] == " ":
                    board[move] = "X"
                    break
                else:
                    print("Oops! That spot is already taken. Try again!")
            except (ValueError, IndexError):
                print("Invalid input. Choose a number from 1 to 9.")

    # AI's move for easy difficulty (random choice)
def ai_move_easy():
        print("\nAI is making its move...")
        time.sleep(1)
        while True:
            move = random.randint(0, 8)
            if board[move] == " ":
                board[move] = "O"
                break

    # AI's move for medium difficulty (block or random)
def ai_move_medium():
        print("\nAI is making its move...")
        time.sleep(1)

        # Check for winning or blocking moves
        for move in range(9):
            if board[move] == " ":
                board[move] = "O"
                if is_winner("O"):
                    return  # AI wins
                board[move] = " "

        for move in range(9):
            if board[move] == " ":
                board[move] = "X"
                if is_winner("X"):
                    board[move] = "O"  # Block player
                    return
                board[move] = " "

        # If no winning or blocking move, pick a random move
        ai_move_easy()

    # AI's move for hard difficulty (minimax algorithm)
def ai_move_hard():
        print("\nAI is thinking hard...")
        time.sleep(1)

        best_score = float('-inf')
        best_move = None

        # Minimax function to evaluate the board
        def minimax(board, depth, is_maximizing):
            if is_winner("O"):
                return 1
            if is_winner("X"):
                return -1
            if is_draw():
                return 0

            if is_maximizing:
                best = float('-inf')
                for i in range(9):
                    if board[i] == " ":
                        board[i] = "O"
                        score = minimax(board, depth + 1, False)
                        board[i] = " "
                        best = max(score, best)
                return best
            else:
                best = float('inf')
                for i in range(9):
                    if board[i] == " ":
                        board[i] = "X"
                        score = minimax(board, depth + 1, True)
                        board[i] = " "
                        best = min(score, best)
                return best

        # Loop through all possible moves and evaluate them using minimax
        for move in range(9):
            if board[move] == " ":
                board[move] = "O"
                score = minimax(board, 0, False)
                board[move] = " "
                if score > best_score:
                    best_score = score
                    best_move = move

        # Make the best move
        board[best_move] = "O"

    # Function to get difficulty level from the user
def get_difficulty():
        while True:
            difficulty = input("\nChoose difficulty level (easy, medium, hard): ").lower()
            if difficulty in ["easy", "medium", "hard"]:
                return difficulty
            else:
                print("Invalid input. Please choose 'easy', 'medium', or 'hard'.")

    # Main game function
def main():
        print("\nWelcome to Tic-Tac-Toe! Let's Play!\n")
        print("You are 'X' and the AI is 'O'.\n")
        print_board()

        # Choose difficulty
        difficulty = get_difficulty()

        # Game loop
        while True:
            player_move()
            print_board()
            if is_winner("X"):
                print("\nCongratulations, you win! 🎉")
                break
            if is_draw():
                print("\nIt's a draw! 😞")
                break

            print("\nAI is making its move...")
            if difficulty == "easy":
                ai_move_easy()
            elif difficulty == "medium":
                ai_move_medium()
            else:  # hard difficulty
                ai_move_hard()

            print_board()
            if is_winner("O"):
                print("\nOh no! The AI wins! 😈")
                break
            if is_draw():
                print("\nIt's a draw! 😞")
                break

    # Run the game
if __name__ == "__main__":
        main()
