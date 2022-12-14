from tkinter import *
 
root = Tk()
root.geometry("430x510")
root.title("Tic Tac Toe GUI")
 
# x is going to start the game - that is computer
 
gameOver = False
 
board = {   1:" " , 2:" " , 3:" " ,
            4:" " , 5:" " , 6:" " ,
            7:" " , 8:" " , 9:" " }
 
buttons = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False , 7:False , 8:False , 9:False}
 
# function to show heading / winner / draw / result
 
def showHeading():
    turnLabel = Label(root , text=f" TIC TAC TOE" , font=("Arial" , 30) , bg="yellow" , relief=SUNKEN , borderwidth=10)
    turnLabel.grid(row = 0 , column=0 , columnspan=3)
 
showHeading()
 
def computerMoveGUI(position):
    if position == 1:
        grid1["text"] = "X"
        
    elif position == 2 :
        grid2["text"] = "X"
        
    elif position == 3 :
        grid3["text"] = "X"
        
    elif position == 4 :
        grid4["text"] = "X"
        
    elif position == 5 :
        grid5["text"] = "X"
        
    elif position == 6 :
        grid6["text"] = "X"
        
    elif position == 7 :
        grid7["text"] = "X"
        
    elif position == 8 :
        grid8["text"] = "X"
        
    elif position == 9 :
        grid9["text"] = "X"
 
# function to change the text of the button
 
def play(event):
    if gameOver:
        return
    grid = event.widget
    gridString = str(grid)
    gridNumber = gridString[-1]
    buttonNumber = 0
    if gridNumber == "n":
        buttonNumber = 1
    else :
        buttonNumber = int(gridNumber)
 
    print(buttonNumber)
    if not buttons[buttonNumber]:
        grid["text"] = "O"
        insertValue(buttonNumber , player)
        buttons[buttonNumber] = True
        
        # computers turn 
        
        buttonNumber = computerMove()
        computerMoveGUI(buttonNumber)
    
 
# ------------------------------ GUI BOARD---------------------------------
 
# first row
 
grid1 = Button(root , text=" ", bg="yellow" , height=1 , width=3 , relief = RAISED , borderwidth = 10 , font=("Arial" , 50))
grid1.grid(row=1 , column=0)
grid1.bind("<Button-1>" , play)
 
grid2 = Button(root , text=" ", bg="yellow" , height=1 , width=3 , relief = RAISED , borderwidth = 10 , font=("Arial" , 50))
grid2.grid(row=1 , column=1)
grid2.bind("<Button-1>" , play)
 
grid3 = Button(root , text=" ", bg="yellow" , height=1 , width=3 , relief = RAISED , borderwidth = 10 , font=("Arial" , 50))
grid3.grid(row=1 , column=2)
grid3.bind("<Button-1>", play)
 
 
# second row
 
grid4 = Button(root , text=" ", bg="yellow" , height=1 , width=3 , relief = RAISED , borderwidth = 10 , font=("Arial" , 50))
grid4.grid(row=2 , column=0)
grid4.bind("<Button-1>", play)
 
grid5 = Button(root , text=" ", bg="yellow" , height=1 , width=3 , relief = RAISED , borderwidth = 10 , font=("Arial" , 50))
grid5.grid(row=2 , column=1)
grid5.bind("<Button-1>", play)
 
grid6 = Button(root , text=" ", bg="yellow" ,height=1 , width=3 , relief = RAISED , borderwidth = 10 , font=("Arial" , 50))
grid6.grid(row=2 , column=2)
grid6.bind("<Button-1>", play)
 
 
# third row
 
grid7 = Button(root , text=" ", bg="yellow" , height=1 , width=3 , relief = RAISED , borderwidth = 10 , font=("Arial" , 50))
grid7.grid(row=3 , column=0)
grid7.bind("<Button-1>", play)
 
grid8 = Button(root , text=" ", bg="yellow" ,height=1 , width=3 , relief = RAISED , borderwidth = 10 , font=("Arial" , 50))
grid8.grid(row=3 , column=1)
grid8.bind("<Button-1>", play)
 
grid9 = Button(root , text=" ", bg="yellow" , height=1 , width=3 , relief = RAISED , borderwidth = 10 , font=("Arial" , 50))
grid9.grid(row=3 , column=2)
grid9.bind("<Button-1>", play)
 
# -------------------- TIC TAC TOE -------------------------------
 
player = "O"
computer = "X"
 
def spaceIsFree(position):
    return board[position] == " " 
 
def checkWhoWin(value):
    if board[1] == board[2] and board[1] == board[3] and board[1] == value:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == value):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == value):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == value):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == value):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == value):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == value):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == value):
        return True
    else:
        return False
 
def checkForDraw():
    for key in board.keys() :
        if board[key] == " " :
            return False 
        
    return True
                    
def insertValue(position , value):
    global gameOver
    if spaceIsFree(position):
        board[position] = value
    else :
        pass
    
    if checkWhoWin(computer) :
        headingLabel = Label(root , text=f"Computer / X wins" , font=("Arial" , 30) , bg="yellow" , relief=SUNKEN , borderwidth=10)
        headingLabel.grid(row = 0 , column=0 , columnspan=3)
        gameOver = True
        
    elif checkWhoWin(player):
        headingLabel = Label(root , text=f"You / O wins" , font=("Arial" , 30) , bg="yellow" , relief=SUNKEN , borderwidth=10)
        headingLabel.grid(row = 0 , column=0 , columnspan=3)
        gameOver = True
      
        
    elif checkForDraw():
        headingLabel = Label(root , text=f"___Game Draw___" , font=("Arial" , 30) , bg="yellow" , relief=SUNKEN , borderwidth=10)
        headingLabel.grid(row = 0 , column=0 , columnspan=3)
        gameOver = True
    
    else :
        pass
    
def minimax(board , isMaximizing):
    
    if checkWhoWin(computer):
        return 1
    
    elif checkWhoWin(player):
        return -1
    
    elif checkForDraw():
        return 0
    
    if isMaximizing :
        bestScore = -100
        for key in board.keys():
            if board[key] == " ":
                board[key] = computer 
                score = minimax(board , False)
                board[key] = " "
                if score > bestScore :
                    bestScore = score
        
        return bestScore 
    
    else :
        bestScore = 100
        for key in board.keys():
            if board[key] == " " :
                board[key] = player 
                score = minimax(board , True)
                board[key] = " "
                if score < bestScore :
                    bestScore = score
                    
        return bestScore
 
def computerMove():
    bestScore = -100
    bestMove = 0
    
    for key in board.keys() :
        if board[key] == " " :
            board[key] = computer
            score = minimax(board , False)
            board[key] = " "
            if score > bestScore :
                bestScore = score 
                bestMove = key
                
    insertValue(bestMove , computer)
    return bestMove
            
computerMoveGUI(computerMove())
 
root.mainloop()
