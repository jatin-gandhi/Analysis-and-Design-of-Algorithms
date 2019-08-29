def partition (array, low,high):	
	pivot = arr[high]
	i = (low - 1) 
	for j in range(low,high-1,1): 
		if array[j] <= pivot: 
			i=i+1 
			temp=array[i]
			array[i]=array[j]
			array[j]=temp 
	temp=array[i+1]
	array[i+1]=array[high]
	array[high]=temp
	return (i + 1) 
 


def quickSort(array,low,high) :
	if low < high :
		pi = partition(arr, low, high) 
		quickSort(arr, low, pi - 1) 
		quickSort(arr, pi + 1, high) 
 


n = int(input("Enter the size of the array"))
arr = list(map(int,input("Enter the elements of array").split()))
quickSort(arr, 0, n-1) 
print("Sorted Array")
for value in arr:
	print(value,end=" ")	

