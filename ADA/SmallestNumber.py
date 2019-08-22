arr = list(map(int,input("Enter the elemets of the array").split()))
k = int(input("Enter the required smallest number"))

for i in range(len(arr)-1):
	for j in range(len(arr)-i-1):
		if arr[j] >arr[j+1] :
			temp = arr[j]
			arr[j]=arr[j+1]
			arr[j+1] = temp

print(k,"Smallest Number",arr[k-1])



#Output
#Enter the elemets of the array 32 -65 12 23 18 -155
#Enter the required smallest number 3
#3 Smallest Number 12

				
