def printBoard(xState, zState):
    symbols = []
    for i in range(9):
        if xState[i]:
            symbols.append('❌')
        elif zState[i]:
            symbols.append('⭕')
        else:
            symbols.append(str(i))

    print("\n")
    print(f" {symbols[0]} | {symbols[1]} | {symbols[2]} ")
    print("---|---|---")
    print(f" {symbols[3]} | {symbols[4]} | {symbols[5]} ")
    print("---|---|---")
    print(f" {symbols[6]} | {symbols[7]} | {symbols[8]} ")
    print("\n")


def checkWin(state):
    wins = [[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
    
    for combo in wins:
        if sum(state[i] for i in combo) == 3:
            return True
    return False


def isDraw(xState, zState):
    return sum(xState) + sum(zState) == 9


def getValidInput(turn, xState, zState):
    while True:
        try:
            value = int(input(f"{'❌ X' if turn == 1 else '⭕ O'}, choose your move (0-8): "))
            if 0 <= value <= 8:
                if not xState[value] and not zState[value]:
                    return value
                else:
                    print("⚠️ That position is already taken. Try again.")
            else:
                print("⚠️ Invalid input. Enter a number between 0 and 8.")
        except ValueError:
            print("⚠️ Please enter a valid number.")


def playGame():
    xState = [0] * 9
    zState = [0] * 9
    turn = 1  # 1 for X, 0 for O

    print("🎮 Welcome to Tic Tac Toe!")
    print("❌ is X and ⭕ is O")
    print("To play, enter the number corresponding to the board position (0-8).")
    
    while True:
        printBoard(xState, zState)
        value = getValidInput(turn, xState, zState)
        if turn == 1:
            xState[value] = 1
            if checkWin(xState):
                printBoard(xState, zState)
                print("🏆 ❌ X won the game!")
                break
        else:
            zState[value] = 1
            if checkWin(zState):
                printBoard(xState, zState)
                print("🏆 ⭕ O won the game!")
                break

        if isDraw(xState, zState):
            printBoard(xState, zState)
            print("🤝 It's a draw!")
            break

        turn = 1 - turn  # Switch turn


def main():
    while True:
        playGame()
        again = input("🔁 Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Thanks for playing Tic Tac Toe!")
            break


if __name__ == "__main__":
    main()