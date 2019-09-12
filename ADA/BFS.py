
import numpy as np

def bfs(adj , i,row,col):
	visited=[0] * (row*row)
	queue=[]
	visited[i] = 1
	queue.append(i)

	while queue:
		j = queue.pop(0)
		print(j+1,end=" ")
		for k in range(1,col):
			if adj[j][k]==1:
				if visited[k] ==0:
					visited[k]=1
					queue.append(k)	




rows,cols = list(map(int,input("Enter the rows and columns\n").split()))

adjacency = list(map(int,input("Enter the adjacency matrix\n").split()))
adjacency = np.array(adjacency).reshape(rows,cols)

print(adjacency)
bfs(adjacency,0,rows,cols)



"""Output:
Enter the rows and columns
9 9
Enter the adjacency matrix
0 1 1 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0 1 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0


[[0 1 1 0 0 0 0 0 0]
 [1 0 0 1 0 0 0 0 0]
 [1 0 0 0 1 1 1 0 0]
 [0 1 0 0 0 0 0 1 0]
 [0 0 1 0 0 0 0 0 0]
 [0 0 1 0 0 0 0 0 1]
 [0 0 1 0 0 0 0 0 0]
 [0 0 0 1 0 0 0 0 0]
 [0 0 0 0 0 1 0 0 0]]


1 2 3 4 5 6 7 8 9


"""
