import numpy as np
def topological(adj,indegree,n):
	"""for i in range(n):
		for j in range(n):
			indegree[i] +=adj[j][i]"""
	length =n	
	while length:

		for i in range(n):
			if indegree[i]==0:
				print(i+1,end=" ")
				indegree[i]=-1
				for j in range(n):
					if adj[i][j]==1:
						indegree[j]=indegree[j]-1
		length -=1



row = int(input("Enter the rows of graph\n"))
print("Enter the adjacency matrix\n")
dependency = list(map(int,input().split()))
dependency = np.array(dependency).reshape(len(dependency)//2,2)
indegree=[0]*row
adjacency =np.zeros((row,row))
row2 = len(dependency)
for i in dependency:
	
	if i[1]==0:
		pass
	else:
		indegree[i[0]-1] +=1
		adjacency[i[1]-1][i[0]-1] = 1
print(dependency)
print()
topological(adjacency,indegree,row)
