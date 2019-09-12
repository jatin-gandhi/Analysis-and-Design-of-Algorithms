import numpy as np


def display(arr): 
    for i in range(9): 
        for j in range(9): 
            print (arr[i][j],end = " ")
        print () 
  
          
def unassigned(arr,l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False
  

def used_row(arr,row,num): 
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False
  

def used_col(arr,col,num): 
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False
  

def used_box(arr,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i+row][j+col] == num): 
                return True
    return False
  

def isSafe(arr,row,col,num): 
  
    return not used_row(arr,row,num) and not used_col(arr,col,num) and not used_box(arr,row - row%3,col - col%3,num) 
  

def sudoku(arr): 
         
    l=[0,0] 
          
    if(not unassigned(arr,l)): 
        return True
      
   
    row=l[0] 
    col=l[1] 
      
  
    for num in range(1,10): 
          
       
        if(isSafe(arr,row,col,num)): 
              
            
            arr[row][col]=num 
  
            if(sudoku(arr)): 
                return True
  
          
            arr[row][col] = 0
              
             
    return False 
  


n = 9
m = 9 
print(n,m)
matrix = []
for i in range(0,m):
    matrix.append([])
    for j in range(0,n):
        matrix[i].append(0)
        matrix[i][j] = int(input())
print matrix
if(sudoku(matrix)): 
	display(matrix) 
else: 
	print ("No solution exists")





"""
Output:


[[3, 0, 6, 5, 0, 8, 4, 0, 0], [5, 2, 0, 0, 0, 0, 0, 0, 0], [0, 8, 7, 0, 0, 0, 0, 3, 1], [0, 0, 3, 0, 1, 0, 0, 8, 0], [9, 0, 0, 8, 6, 3, 0, 0, 5], [0, 5, 0, 0, 9, 0, 6, 0, 0], [1, 3, 0, 0, 0, 0, 2, 5, 0], [0, 0, 0, 0, 0, 0, 0, 7, 4], [0, 0, 5, 2, 0, 6, 3, 0, 0]]


3 1 6 5 7 8 4 9 2 
5 2 9 1 3 4 7 6 8 
4 8 7 6 2 9 5 3 1 
2 6 3 4 1 5 9 8 7 
9 7 4 8 6 3 1 2 5 
8 5 1 7 9 2 6 4 3 
1 3 8 9 4 7 2 5 6 
6 9 2 3 5 1 8 7 4 
7 4 5 2 8 6 3 1 9 
"""
