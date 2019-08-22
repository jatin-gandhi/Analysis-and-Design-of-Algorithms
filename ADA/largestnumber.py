array = list(map(int,input("Enter the elemets of the array").split()))
k = int(input("Enter the required largest numbers"))

for i in range(len(array)-1):
	for j in range(len(array)-i-1):
		if array[j] < array[j+1] :
			temp = array[j]
			array[j]=array[j+1]
			array[j+1] = temp


print(k,"Largest Numbers ",array[:k])




#Output
#Enter the elemets of the array 32 -65 12 23 18 -155
#Enter the required largest numbers3
#3 Largest Numbers  [32, 23, 18]


