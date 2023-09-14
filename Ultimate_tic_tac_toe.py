import time

def display_grid(grid):
    for row in range(3):
        for sub_row in range(3):
            for column in range(3):
                for sub_column in range(3):
                    cell_value = grid[row * 3 + column][sub_row * 3 + sub_column]
                    if cell_value == 0:
                        print(" ", end=" ")
                    elif cell_value == 1:
                        print("X", end=" ")
                    elif cell_value == -1:
                        print("O", end=" ")
                    else:
                        print(cell_value, end=" ")
                    if sub_column < 2:
                        print("|", end=" ")
                if column < 2:
                    print("#", end="  ")
            print("")
        if row < 2:
            print("-" * 35)

def check_win_tic_tac_toe_case_with_draw(grid_tic_tac_toe): 
    player_1 = 1
    if (grid_tic_tac_toe[0] + grid_tic_tac_toe[1] + grid_tic_tac_toe[2] == player_1 * 3 or
        grid_tic_tac_toe[3] + grid_tic_tac_toe[4] + grid_tic_tac_toe[5] == player_1 * 3 or
        grid_tic_tac_toe[6] + grid_tic_tac_toe[7] + grid_tic_tac_toe[8] == player_1 * 3 or
        grid_tic_tac_toe[0] + grid_tic_tac_toe[3] + grid_tic_tac_toe[6] == player_1 * 3 or
        grid_tic_tac_toe[1] + grid_tic_tac_toe[4] + grid_tic_tac_toe[7] == player_1 * 3 or
        grid_tic_tac_toe[2] + grid_tic_tac_toe[5] + grid_tic_tac_toe[8] == player_1 * 3 or
        grid_tic_tac_toe[0] + grid_tic_tac_toe[4] + grid_tic_tac_toe[8] == player_1 * 3 or
        grid_tic_tac_toe[2] + grid_tic_tac_toe[4] + grid_tic_tac_toe[6] == player_1 * 3):
        return player_1

    player_2 = -1
    if (grid_tic_tac_toe[0] + grid_tic_tac_toe[1] + grid_tic_tac_toe[2] == player_2 * 3 or
        grid_tic_tac_toe[3] + grid_tic_tac_toe[4] + grid_tic_tac_toe[5] == player_2 * 3 or
        grid_tic_tac_toe[6] + grid_tic_tac_toe[7] + grid_tic_tac_toe[8] == player_2 * 3 or
        grid_tic_tac_toe[0] + grid_tic_tac_toe[3] + grid_tic_tac_toe[6] == player_2 * 3 or
        grid_tic_tac_toe[1] + grid_tic_tac_toe[4] + grid_tic_tac_toe[7] == player_2 * 3 or
        grid_tic_tac_toe[2] + grid_tic_tac_toe[5] + grid_tic_tac_toe[8] == player_2 * 3 or
        grid_tic_tac_toe[0] + grid_tic_tac_toe[4] + grid_tic_tac_toe[8] == player_2 * 3 or
        grid_tic_tac_toe[2] + grid_tic_tac_toe[4] + grid_tic_tac_toe[6] == player_2 * 3):
        return player_2

    if any(i == 0 for i in grid_tic_tac_toe):
        return 0

    return -100

def check_win_tic_tac_toe(grid_tic_tac_toe): 
    player_1 = 1
    if (grid_tic_tac_toe[0] + grid_tic_tac_toe[1] + grid_tic_tac_toe[2] == player_1 * 3 or
        grid_tic_tac_toe[3] + grid_tic_tac_toe[4] + grid_tic_tac_toe[5] == player_1 * 3 or
        grid_tic_tac_toe[6] + grid_tic_tac_toe[7] + grid_tic_tac_toe[8] == player_1 * 3 or
        grid_tic_tac_toe[0] + grid_tic_tac_toe[3] + grid_tic_tac_toe[6] == player_1 * 3 or
        grid_tic_tac_toe[1] + grid_tic_tac_toe[4] + grid_tic_tac_toe[7] == player_1 * 3 or
        grid_tic_tac_toe[2] + grid_tic_tac_toe[5] + grid_tic_tac_toe[8] == player_1 * 3 or
        grid_tic_tac_toe[0] + grid_tic_tac_toe[4] + grid_tic_tac_toe[8] == player_1 * 3 or
        grid_tic_tac_toe[2] + grid_tic_tac_toe[4] + grid_tic_tac_toe[6] == player_1 * 3):
        return player_1

    player_2 = -1
    if (grid_tic_tac_toe[0] + grid_tic_tac_toe[1] + grid_tic_tac_toe[2] == player_2 * 3 or
        grid_tic_tac_toe[3] + grid_tic_tac_toe[4] + grid_tic_tac_toe[5] == player_2 * 3 or
        grid_tic_tac_toe[6] + grid_tic_tac_toe[7] + grid_tic_tac_toe[8] == player_2 * 3 or
        grid_tic_tac_toe[0] + grid_tic_tac_toe[3] + grid_tic_tac_toe[6] == player_2 * 3 or
        grid_tic_tac_toe[1] + grid_tic_tac_toe[4] + grid_tic_tac_toe[7] == player_2 * 3 or
        grid_tic_tac_toe[2] + grid_tic_tac_toe[5] + grid_tic_tac_toe[8] == player_2 * 3 or
        grid_tic_tac_toe[0] + grid_tic_tac_toe[4] + grid_tic_tac_toe[8] == player_2 * 3 or
        grid_tic_tac_toe[2] + grid_tic_tac_toe[4] + grid_tic_tac_toe[6] == player_2 * 3):
        return player_2

    return 0 

def evaluateGame(grid, grid_to_play):
    eval_value = 0 
    main_board = []
    morpion_weights = [1.4, 1, 1.4, 1, 1.75, 1, 1.4, 1, 1.4] 

    for i in range(9):
        eval_value += evaluate_tic_tac_toe(grid[i]) * 1.5 * morpion_weights[i]

        if i == grid_to_play:
            eval_value += evaluate_tic_tac_toe(grid[i]) * morpion_weights[i]

        tmp_eval = check_win_tic_tac_toe(grid[i]) 
        eval_value -= tmp_eval * morpion_weights[i] 
        main_board.append(tmp_eval) 

    eval_value -= check_win_tic_tac_toe(main_board) * 5000 
    eval_value += evaluate_tic_tac_toe(main_board) * 150 
    return eval_value

def evaluate_tic_tac_toe(position): #position = a tic-tac-toe grid
    evaluation = 0
    weights = [0.2, 0.17, 0.2, 0.17, 0.22, 0.17, 0.2, 0.17, 0.2]  #Base weights of a tic-tac-toe grid (middle has higher weight, corners have less, and in-between have a moderate weight)

    for i in range(len(position)): #To see who has a favorable position
        evaluation -= position[i] * weights[i]

    player_X = -2 # The computer has O O aligned, so high score because it wins if it places
    if (position[0] + position[1] + position[2] == player_X or
        position[3] + position[4] + position[5] == player_X or
        position[6] + position[7] + position[8] == player_X):
        evaluation += 6
    if (position[0] + position[3] + position[6] == player_X or
        position[1] + position[4] + position[7] == player_X or
        position[2] + position[5] + position[8] == player_X):
        evaluation += 6
    if (position[0] + position[4] + position[8] == player_X or
        position[2] + position[4] + position[6] == player_X):
        evaluation += 7

    player_O = 1 # Player has 1 empty cell, and if the other 2 cells are also empty, we give +9 to encourage the AI to block it
    if ((position[0] + position[1] == 2*player_O and position[2] == -player_O) or
        (position[1] + position[2] == 2*player_O and position[0] == -player_O) or
        (position[0] + position[2] == 2*player_O and position[1] == -player_O) or
        (position[3] + position[4] == 2*player_O and position[5] == -player_O) or
        (position[3] + position[5] == 2*player_O and position[4] == -player_O) or
        (position[5] + position[4] == 2*player_O and position[3] == -player_O) or
        (position[6] + position[7] == 2*player_O and position[8] == -player_O) or
        (position[6] + position[8] == 2*player_O and position[7] == -player_O) or
        (position[7] + position[8] == 2*player_O and position[6] == -player_O) or
        (position[0] + position[3] == 2*player_O and position[6] == -player_O) or
        (position[0] + position[6] == 2*player_O and position[3] == -player_O) or
        (position[3] + position[6] == 2*player_O and position[0] == -player_O) or
        (position[1] + position[4] == 2*player_O and position[7] == -player_O) or
        (position[1] + position[7] == 2*player_O and position[4] == -player_O) or
        (position[4] + position[7] == 2*player_O and position[1] == -player_O) or
        (position[2] + position[5] == 2*player_O and position[8] == -player_O) or
        (position[2] + position[8] == 2*player_O and position[5] == -player_O) or
        (position[5] + position[8] == 2*player_O and position[2] == -player_O) or
        (position[0] + position[4] == 2*player_O and position[8] == -player_O) or
        (position[0] + position[8] == 2*player_O and position[4] == -player_O) or
        (position[4] + position[8] == 2*player_O and position[0] == -player_O) or
        (position[2] + position[4] == 2*player_O and position[6] == -player_O) or
        (position[2] + position[6] == 2*player_O and position[4] == -player_O) or
        (position[4] + position[6] == 2*player_O and position[2] == -player_O)):
        evaluation += 9

    player_X = 2 # If a=2, it means player 1 (Human) has X X, so we need to block, hence high score
    if (position[0] + position[1] + position[2] == player_X or
        position[3] + position[4] + position[5] == player_X or
        position[6] + position[7] + position[8] == player_X): #Rows
        evaluation -= 6
    if (position[0] + position[3] + position[6] == player_X or
        position[1] + position[4] + position[7] == player_X or
        position[2] + position[5] + position[8] == player_X): #Columns
        evaluation -= 6
    if (position[0] + position[4] + position[8] == player_X or
        position[2] + position[4] + position[6] == player_X): #Diagonals
        evaluation -= 7

    computer_O = -1 # The computer (-1) only has one O
    if ((position[0] + position[1] == 2*computer_O and position[2] == -computer_O) or
        (position[1] + position[2] == 2*computer_O and position[0] == -computer_O) or
        (position[0] + position[2] == 2*computer_O and position[1] == -computer_O) or
        (position[3] + position[4] == 2*computer_O and position[5] == -computer_O) or
        (position[3] + position[5] == 2*computer_O and position[4] == -computer_O) or
        (position[5] + position[4] == 2*computer_O and position[3] == -computer_O) or
        (position[6] + position[7] == 2*computer_O and position[8] == -computer_O) or
        (position[6] + position[8] == 2*computer_O and position[7] == -computer_O) or
        (position[7] + position[8] == 2*computer_O and position[6] == -computer_O) or
        (position[0] + position[3] == 2*computer_O and position[6] == -computer_O) or
        (position[0] + position[6] == 2*computer_O and position[3] == -computer_O) or
        (position[3] + position[6] == 2*computer_O and position[0] == -computer_O) or
        (position[1] + position[4] == 2*computer_O and position[7] == -computer_O) or
        (position[1] + position[7] == 2*computer_O and position[4] == -computer_O) or
        (position[4] + position[7] == 2*computer_O and position[1] == -computer_O) or
        (position[2] + position[5] == 2*computer_O and position[8] == -computer_O) or
        (position[2] + position[8] == 2*computer_O and position[5] == -computer_O) or
        (position[5] + position[8] == 2*computer_O and position[2] == -computer_O) or
        (position[0] + position[4] == 2*computer_O and position[8] == -computer_O) or
        (position[0] + position[8] == 2*computer_O and position[4] == -computer_O) or
        (position[4] + position[8] == 2*computer_O and position[0] == -computer_O) or
        (position[2] + position[4] == 2*computer_O and position[6] == -computer_O) or
        (position[2] + position[6] == 2*computer_O and position[4] == -computer_O) or
        (position[4] + position[6] == 2*computer_O and position[2] == -computer_O)):
        evaluation -= 9  #We subtract 9 for a defensive approach, we prioritize blocking player 1 (with a=1 +9) over playing for ourselves

    evaluation -= check_win_tic_tac_toe(position)*12  #Score reduced by 12 if player 1 is winning. ATTENTION if it's computer then eval - (-1)*12 = eval + 12 !!

    return evaluation

# Minimax
def miniMax(grid, boardToPlayOn, depth, alpha, beta, isMaxPlayer):

    tmpPlayer = -1  # Position where we will play
    calcEval = evaluateGame(grid, boardToPlayOn)
    
    if depth <= 0 or abs(calcEval) > 5000:  # Stopping condition
        return {"mE": calcEval, "tP": tmpPlayer}  # "mE" (for maxEval or minEval) and "tP" (for tmpPlayer)"
    
    if boardToPlayOn != -1 and check_win_tic_tac_toe(grid[boardToPlayOn]) != 0: # Checks if the player can play on a tic-tac-toe board, otherwise returns -1, meaning can play anywhere
        boardToPlayOn = -1
    
    if boardToPlayOn != -1 and 0 not in grid[boardToPlayOn]: # Takes a draw case
        boardToPlayOn = -1
    
    if isMaxPlayer:
        maxEval = -float('inf')
        for tic_tac_toe in range(9):
            evalut = -float('inf')  # temporary in the end maxEval = evalut
            evalut_dict = {"mE": -float('inf'), "tP": -1}
            # If we can play anywhere, do them all:
            if boardToPlayOn == -1:
                for position in range(9):
                    if check_win_tic_tac_toe(grid[tic_tac_toe]) == 0:  # Take only those which are not yet finished

                        if grid[tic_tac_toe][position] == 0:
                            grid[tic_tac_toe][position] = -1  # AI places an O
                            evalut = miniMax(grid, position, depth-1, alpha, beta, False)["mE"]  # return {"mE": calcEval, "tP": tmpPlayer}  Get calcEval
                            grid[tic_tac_toe][position] = 0  # Prevents changing the grid
                        if evalut > maxEval:
                            maxEval = evalut
                            tmpPlayer = tic_tac_toe

                        alpha = max(alpha, evalut)  # Classic part of minmax pruning
                    if beta <= alpha:
                        break
            else:  # If we have to play on a particular board
                if grid[boardToPlayOn][tic_tac_toe] == 0:
                    grid[boardToPlayOn][tic_tac_toe] = -1
                    evalut_dict = miniMax(grid, tic_tac_toe, depth-1, alpha, beta, False)
                    grid[boardToPlayOn][tic_tac_toe] = 0
                
                tempMaxi = evalut_dict["mE"]
                
                if tempMaxi > maxEval:
                    maxEval = tempMaxi
                    tmpPlayer = evalut_dict["tP"]
                
                alpha = max(alpha, tempMaxi)
                
                if beta <= alpha:
                    break
        
        return {"mE": maxEval, "tP": tmpPlayer}
    
    else:  # Same for min
        minEval = float('inf')
        for tic_tac_toe in range(9):
            evalua = float('inf')
            evalua_dict = {"mE": float('inf'), "tP": -1}
            
            if boardToPlayOn == -1:
                for position in range(9):
                    if check_win_tic_tac_toe(grid[tic_tac_toe]) == 0:
                        if grid[tic_tac_toe][position] == 0:
                            grid[tic_tac_toe][position] = 1  # Player 1
                            evalua = miniMax(grid, position, depth-1, alpha, beta, True)["mE"]
                            grid[tic_tac_toe][position] = 0
                        if evalua < minEval:
                            minEval = evalua
                            tmpPlayer = tic_tac_toe
                        beta = min(beta, evalua)
                    if beta <= alpha:
                        break
            else:
                if grid[boardToPlayOn][tic_tac_toe] == 0:
                    grid[boardToPlayOn][tic_tac_toe] = 1
                    evalua_dict = miniMax(grid, tic_tac_toe, depth-1, alpha, beta, True)
                    grid[boardToPlayOn][tic_tac_toe] = 0
                
                tempMini = evalua_dict["mE"]
                
                if tempMini < minEval:
                    minEval = tempMini
                    tmpPlayer = evalua_dict["tP"]

                beta = min(beta, tempMini)
                if beta <= alpha:
                    break
        
        return {"mE": minEval, "tP": tmpPlayer}


# Determines where the AI should move to win the regular Tic Tac Toe 
# (different from evaluateMorpion because here it's to know where to place)
def evaluatePosition(tic_tac_toe, positionInTicTacToe):  # pos represents 1 tic-tac-toe (1 line)
    
    tic_tac_toe[positionInTicTacToe] = -1  # We place our mark in a tic-tac-toe
    evaluation = 0
    
    # Preference for the center, then the corners, and finally the edges
    points = [0.2, 0.17, 0.2, 0.17, 0.22, 0.17, 0.2, 0.17, 0.2]
    evaluation += points[positionInTicTacToe]
    
    # Preference for creating pairs
    a = -2
    if (tic_tac_toe[0] + tic_tac_toe[1] + tic_tac_toe[2] == a or tic_tac_toe[3] + tic_tac_toe[4] + tic_tac_toe[5] == a or tic_tac_toe[6] + tic_tac_toe[7] + tic_tac_toe[8] == a or 
        tic_tac_toe[0] + tic_tac_toe[3] + tic_tac_toe[6] == a or tic_tac_toe[1] + tic_tac_toe[4] + tic_tac_toe[7] == a or tic_tac_toe[2] + tic_tac_toe[5] + tic_tac_toe[8] == a or 
        tic_tac_toe[0] + tic_tac_toe[4] + tic_tac_toe[8] == a or tic_tac_toe[2] + tic_tac_toe[4] + tic_tac_toe[6] == a):
        evaluation += 1
    
    # Preference for victory
    a = -3
    if (tic_tac_toe[0] + tic_tac_toe[1] + tic_tac_toe[2] == a or tic_tac_toe[3] + tic_tac_toe[4] + tic_tac_toe[5] == a or tic_tac_toe[6] + tic_tac_toe[7] + tic_tac_toe[8] == a or 
        tic_tac_toe[0] + tic_tac_toe[3] + tic_tac_toe[6] == a or tic_tac_toe[1] + tic_tac_toe[4] + tic_tac_toe[7] == a or tic_tac_toe[2] + tic_tac_toe[5] + tic_tac_toe[8] == a or 
        tic_tac_toe[0] + tic_tac_toe[4] + tic_tac_toe[8] == a or tic_tac_toe[2] + tic_tac_toe[4] + tic_tac_toe[6] == a):
        evaluation += 5
    
    # Opponent blocking
    tic_tac_toe[positionInTicTacToe] = 1
    a = 3
    if (tic_tac_toe[0] + tic_tac_toe[1] + tic_tac_toe[2] == a or tic_tac_toe[3] + tic_tac_toe[4] + tic_tac_toe[5] == a or tic_tac_toe[6] + tic_tac_toe[7] + tic_tac_toe[8] == a or 
        tic_tac_toe[0] + tic_tac_toe[3] + tic_tac_toe[6] == a or tic_tac_toe[1] + tic_tac_toe[4] + tic_tac_toe[7] == a or tic_tac_toe[2] + tic_tac_toe[5] + tic_tac_toe[8] == a or 
        tic_tac_toe[0] + tic_tac_toe[4] + tic_tac_toe[8] == a or tic_tac_toe[2] + tic_tac_toe[4] + tic_tac_toe[6] == a):
        evaluation += 2
    
    # Checking win conditions
    tic_tac_toe[positionInTicTacToe] = -1
    evaluation -= check_win_tic_tac_toe(tic_tac_toe) * 15
    tic_tac_toe[positionInTicTacToe] = 0
    
    return evaluation

# Game operation
def winner_function(grid):  # Know who is the winner of the ultimate tic-tac-toe
    boards = []
    for i in range(len(grid)):
        winner = check_win_tic_tac_toe_case_with_draw(grid[i])
        boards.append(winner)
    # print(boards)
    return check_win_tic_tac_toe_case_with_draw(boards)

def check_win(grid):  # Know if the game is finished or not
    winner = winner_function(grid)  # Get player 1 or 2 or draw
    if winner == 1 or winner == -1 or winner == -100:
        return True
    else:
        return False

def main():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print("Welcome to Ultimate Tic Tac Toe!")
    display_grid(grid)

    current_turn = -1
    moves = 0
    total_execution_time = 0
    start_time = 0
    end_time = 0

    while True:
        try:
            turn = int(input("Which player wants to start? Player 1 type 1, Computer starts type -1: "))
            if turn not in [1, -1]:
                raise ValueError("Enter 1 or -1")
            current_turn = turn
            break
        except ValueError as e:
            print(e)

    if current_turn == 1:
        move_morpion = input("Player 1 (X), choose a tic-tac-toe (1-9): ")
        current_board = int(move_morpion) - 1
    else:
        current_board = -1

    while not check_win(grid):
        if current_turn == 1:
            if check_win_tic_tac_toe(grid[current_board]) != 0:
                move_morpion = input("Player 1 (X), choose a TIC TAC TOE (1-9): ")
                current_board = int(move_morpion) - 1
            move_case = input("Player 1 (X), enter your move (1-9): ")

            try:
                if grid[current_board][int(move_case) - 1] == 0:
                    grid[current_board][int(move_case) - 1] = current_turn
                    current_board = int(move_case) - 1
                    current_turn = -1
                else:
                    print("This case is already occupied, please choose another case.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")

        else:
            moves += 1
            print(f"Move number: {moves}")
            print("The computer (O) is playing...")
            start_time = time.time()

            best_move = -1
            best_score = [-float('inf')] * 9
            count = 0

            for i in range(len(grid)):
                if check_win_tic_tac_toe(grid[i]) == 0:
                    count += sum([1 for v in grid[i] if v == 0])

            if current_board == -1 or check_win_tic_tac_toe(grid[current_board]) != 0:
                tmp_minimax = None
                print("Remaining: ", count)

                if moves < 10:
                    tmp_minimax = miniMax(grid, -1, min(4, count), -float('inf'), float('inf'), True)
                elif moves < 18:
                    tmp_minimax = miniMax(grid, -1, min(5, count), -float('inf'), float('inf'), True)
                else:
                    tmp_minimax = miniMax(grid, -1, min(5, count), -float('inf'), float('inf'), True)

                current_board = tmp_minimax["tP"]

            for i in range(9):
                if grid[current_board][i] == 0:
                    best_move = i
                    break

            if best_move != -1:
                for a in range(9):
                    if grid[current_board][a] == 0:
                        score = evaluatePosition(grid[current_board], a) * 45
                        best_score[a] = score

                for b in range(9):
                    if check_win_tic_tac_toe(grid[current_board]) == 0:
                        if grid[current_board][b] == 0:
                            grid[current_board][b] = -1

                            if (moves < 20 or time.time() - start_time > 4):
                                tmp_minimax = miniMax(grid, b, min(4, count), -float("inf"), float("inf"), False)
                            elif moves < 36:
                                tmp_minimax = miniMax(grid, b, min(5, count), -float("inf"), float("inf"), False)
                            else:
                                tmp_minimax = miniMax(grid, b, min(6, count), -float("inf"), float("inf"), False)

                            score2 = tmp_minimax["mE"]
                            grid[current_board][b] = 0
                            best_score[b] += score2

                for i in range(9):
                    if best_score[i] > best_score[best_move]:
                        best_move = i

                if grid[current_board][best_move] == 0:
                    grid[current_board][best_move] = -1
                    print(f"The computer played in the tic-tac-toe: {current_board+1} and the case {best_move+1}")
                    current_board = best_move

                print(f"The player must play in the tic-tac-toe: {current_board+1}")

                end_time = time.time()
                execution_time = end_time - start_time
                total_execution_time += execution_time
                print(f"The execution time is: {execution_time}")

            current_turn = -current_turn
        display_grid(grid)

    winner = winner_function(grid)

    if winner == -100:
        print("It's a draw!")
    else:
        print(f"The winner is {'Player 1 (X)' if winner == 1 else 'Computer (O)'}!")
    print(f"The total execution time is: {total_execution_time}")

if __name__ == "__main__":
    main()
