import copy

VIC = 10 ** 20  # The value of a winning board (for max)
LOSS = -VIC  # The value of a losing board (for max)
TIE = 0  # The value of a tie
SIZE = 3  # The length of a winning sequence
COMPUTER = SIZE + 1  # Marks the computer's cells on the board
HUMAN = 1  # Marks the human's cells on the board

'''
The state of the game is represented by a list of 4 items:
0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
   the comp's cells = COMPUTER and the human's = HUMAN
1. The heuristic value of the state.
2. Who's turn is it: HUMAN or COMPUTER
3. number of empty cells
'''


def create():
    # Returns an empty board. The human plays first.
    board = []
    for i in range(3):
        board = board + [3 * [0]]
    return [board, 0.00001, HUMAN, 9]


def value(s):
    # Returns the heuristic value of s
    return s[1]


def printState(s):
    # Prints the board. The empty cells are printed as numbers = the cells name(for input)
    # If the game ended prins who won.
    for r in range(len(s[0])):
        print("\n -- -- --\n|", end="")
        for c in range(len(s[0][0])):
            if s[0][r][c] == COMPUTER:
                print("X |", end="")
            elif s[0][r][c] == HUMAN:
                print("O |", end="")
            else:
                print(r * 3 + c, "|", end="")
    print("\n -- -- --\n")
    if value(s) == VIC:
        print("Ha ha ha I won!")
    elif value(s) == LOSS:
        print("You did it!")
    elif value(s) == TIE:
        print("It's a TIE")


def isFinished(s):
    # Seturns True iff the game ended
    return s[1] in [LOSS, VIC, TIE]


def isHumTurn(s):
    # Returns True iff it the human's turn to play
    return s[2] == HUMAN


def whoIsFirst(s):
    # The user decides who plays first
    if int(input("Who plays first? 1-me / anything else-you. : ")) == 1:
        s[2] = COMPUTER
    else:
        s[2] == HUMAN


def checkSeq(s, r1, c1, r2, c2):
    # r1, c1 are in the board. if r2,c2 not on board returns 0.
    # Checks the seq. from r1,c1 to r2,c2. If all X returns VIC. If all O returns LOSS.
    # If no Os returns 1. If no Xs returns -1, Othewise returns 0.
    if r2 < 0 or c2 < 0 or r2 >= len(s[0]) or c2 >= len(s[0][0]):
        return 0  # r2, c2 are illegal
    dr = (r2 - r1) // (SIZE - 1)  # the horizontal step from cell to cell
    dc = (c2 - c1) // (SIZE - 1)  # the vertical step from cell to cell
    sum = 0
    for i in range(SIZE):  # summing the values in the seq.
        sum += s[0][r1 + i * dr][c1 + i * dc]
    if sum == COMPUTER * SIZE:
        return VIC
    if sum == HUMAN * SIZE:
        return LOSS
    if sum > 0 and sum < COMPUTER:
        return -1
    if sum > 0 and sum % COMPUTER == 0:
        return 1
    return 0


def makeMove(s, r, c):
    # Puts mark (for huma. or comp.) in r,c
    # switches turns
    # and re-evaluates the heuristic value.
    # Assumes the move is legal.
    s[0][r][c] = s[2]  # marks the board
    s[3] -= 1  # one less empty cell
    s[2] = COMPUTER + HUMAN - s[2]  # switches turns
    dr = [-SIZE + 1, -SIZE + 1, 0, SIZE - 1]  # the next lines compute the heuristic val.
    dc = [0, SIZE - 1, SIZE - 1, SIZE - 1]
    s[1] = 0.00001
    for row in range(len(s[0])):
        for col in range(len(s[0][0])):
            for i in range(len(dr)):
                t = checkSeq(s, row, col, row + dr[i], col + dc[i])
                if t in [LOSS, VIC]:
                    s[1] = t
                    return
                else:
                    s[1] += t
    if s[3] == 0:
        s[1] = TIE


def inputMove(s):
    # Reads, enforces legality and executes the user's move.
    printState(s)
    flag = True
    while flag:
        move = int(input("Enter your next move: "))
        r = move // 3
        c = move % 3
        if r < 0 or r >= len(s[0]) or c < 0 or c >= len(s[0][0]) or s[0][r][c] != 0:
            print("Ilegal move.")
        else:
            flag = False
            makeMove(s, r, c)


def getNext(s):
    # returns a list of the next states of s
    ns = []
    for r in range(len(s[0])):
        for c in range(len(s[0][0])):
            if s[0][r][c] == 0:
                tmp = copy.deepcopy(s)
                makeMove(tmp, r, c)
                ns += [tmp]
    return ns

