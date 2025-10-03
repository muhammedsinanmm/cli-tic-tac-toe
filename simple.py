from colorama import Fore, Style, init
init(autoreset=True)


def getSymbol(sym):
    if sym == "x":
        return Fore.RED + "X" + Style.RESET_ALL
    elif sym == "o":
        return Fore.BLUE + "O" + Style.RESET_ALL
    return " "



def printBoard():
    
    print("", getSymbol(board[0]), "|", getSymbol(board[1]), "|", getSymbol(board[2]))
    print("---|---|---")
    print("", getSymbol(board[3]), "|", getSymbol(board[4]), "|", getSymbol(board[5]))
    print("---|---|---")
    print("", getSymbol(board[6]), "|", getSymbol(board[7]), "|", getSymbol(board[8]))


def checkWinner():
    
    for i in range(0,7,3):
        if board[i] != " " and board[i]==board[i+1]==board[i+2]:
            print(board[i],"Player Won")
            return True
    for i in range(3):
        if board[i] != " " and board[i]==board[i+3]==board[i+6]:
            print(board[i],"Player Won")
            return True
    if board[0]!= " " and board[0]==board[4]==board[8]:
        print(board[0],"Player Won")
        return True
        
    elif board[2] != " " and board[2]==board[4]==board[6]:
        print(board[2],"Player Won")
        return True
    if board.count(" ") == 0:
        print("Draw")
        return True
    return False
    
def doAgain():
    global running,board
    choice = input("Do you wanna continue (y/n): ")
    if choice.lower() == 'y':
        running = True
        board = [" "]*9
        printBoard()
    else:
        running = False    

def makeMove(xox):
    while True:
        try:
            move = int(input(f"Type where you want to place your {xox} : "))
            if move <0 or move >8:
                print("please enter a valid index of the box")
                continue
            if board[move] != " ":
                print("The column is already taken")
                continue
            board[move] = xox
            break
        except ValueError:
            print("Enter a valid number between 0 to 8")
            
        
            
        
        
        
        

 
board = [" "]*9
printBoard()
running = True
while  running:
    
    
        
    if checkWinner():
        break
    print("The box consist of index 0 to 8.type the box number where you want to put corresponding 'x' or 'o' ")
    print("Player one's turn: put 'x'")
    makeMove('x')
    printBoard()
    
    if checkWinner():
        doAgain()
        continue
    
    print("Player two's turn: put 'o' ")
    makeMove('o')
    printBoard()
    if checkWinner():
        doAgain()
        continue
    
