def tic_tac_toe(board):
    winning = "Draw"
    down = []
    down2 = []
    down3 = []
    dia1 = []
    dia2 = []
    across = []
    across2 = []
    across3 = []
    across = board[0]
    across2 = board[1]
    across3 = board[2]
    for i in board:
        down.append(i[0])
        down2.append(i[1])
        down3.append(i[2])
    for i in range(3):
        dia1.append(board[i-1][i-1])
    count = 2
    for i in range(3):
        dia2.append(board[count][i])
        count -= 1
    y = dia1 
    for i in range(8):
        if i == 2:
            y = dia2
        elif i == 3:
            y = down
        elif i == 4:
            y = down2
        elif i == 5:
            y = down3
        elif i == 6:
            y = across
        elif i == 7:
            y = across2
        elif i == 8:
            y = across3
        if "X" not in y:
            if "E" not in y:
                winning = "O"
        elif "O" not in y:
            if "E" not in y:
                winning = "X"
    return winning

print(tic_tac_toe([
	["X", "X", "O"],
	["O", "O", "X"],
	["X", "X", "O"]
]))