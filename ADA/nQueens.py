def isSafe(board, row, col,N):       
    for i in range(col): 
        if board[row][i] == 1: 
            return False
    for i, j in zip(range(row, -1, -1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
    for i, j in zip(range(row, N, 1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    return True
  
def queenCheck(board, col,N): 
    if col >= N: 
        return True    
    for i in range(N):  
        if isSafe(board, i, col,N):                        
            board[i][col] = 1             
            if queenCheck(board, col + 1,N) == True: 
                return True
            board[i][col] = 0    
    return False
  
def display(board,N): 
    for i in range(N): 
        for j in range(N): 
            print (board[i][j], end = " ") 
        print() 

def nqueen(N): 
    board = [ [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0] ] 
  
    if queenCheck(board, 0,N) == False: 
        print ("No Solution") 
        return False
  
    display(board,N) 
    return True
  
N = int(input("Enter the size\n"))
nqueen(N) 
