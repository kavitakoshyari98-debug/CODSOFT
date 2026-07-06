import math

HUMAN = "X"
AI = "O"

board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print("\n")


def print_positions():
    print("Board Positions:")
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 ")
    print()


def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_draw():
    return " " not in board
def minimax(is_maximizing):
    if check_winner(AI):
        return 1
    if check_winner(HUMAN):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = AI
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = AI

    def human_move():
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8:
                print("Choose a number between 0 and 8.")
            elif board[move] != " ":
                print("That position is already taken.")
            else:
                board[move] = HUMAN
                break
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("===== TIC TAC TOE AI =====")
    print("You are X")
    print("AI is O")
    print_positions()

    while True:
        print_board()

        human_move()

        if check_winner(HUMAN):
            print_board()
            print("🎉 Congratulations! You Win!")
            break

        if is_draw():
            print_board()
            print("It's a Draw!")
            break

        print("AI is thinking...\n")
        ai_move()

        if check_winner(AI):
            print_board()
            print("🤖 AI Wins!")
            break

        if is_draw():
            print_board()
            print("It's a Draw!")
            break


if __name__ == "__main__":
    main()