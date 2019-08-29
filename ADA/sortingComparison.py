import numpy as np
total_merge= 0
total_bubble = 0
total_selection = 0
def merge(arr, l, m, r):
   
    m = int(m )
    r = int(r)
    l = int(l)
    n1 = (m - l + 1)
    n2 = (r- m)  
    L = [0] * (n1) 
    R = [0] * (n2) 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
    i = 0    
    j = 0  
    k = l   
    global total_merge
    while i < n1 and j < n2 : 
        total_merge = total_merge+1
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  

def mergeSort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))/2
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 



def bubbleSort(array):
	global total_bubble
	for i in range(len(array)-1):
		for j in range(len(array)-i-1):
			total_bubble = total_bubble+1
			if array[j] > array[j+1] :
				temp = array[j]
				array[j]=array[j+1]
				array[j+1] = temp
	return array


def selectionSort(array,size):
    global total_selection
    for i in range(size):
        position = i
        for j in range(i + 1, size):
            total_selection = total_selection +  1
            if array[position] > array[j]:
                position = j
        array[i], array[position] = array[position], array[i]
    return array

  


n = int(input("Enter the size of the array"))
arr = list(map(int,np.random.random_sample(n) *100))
array1 = arr
array2 = arr
array3 = arr
bubbleSort(array1) 
print("\n BUBBLE SORT \n\n Sorted Array:")
for value in array1:
	print(value,end=" ")

print("\n Comaprisons :",total_bubble)	


selectionSort(array2,n) 
print("\n SELECTION SORT \n\n Sorted Array:")
for value in array2:
	print(value,end=" ")

print("\n Comaprisons:",total_selection)


mergeSort(array3,0,n-1) 
print("\n MERGE SORT \n\n Sorted Array:")
for value in array3:
	print(value,end=" ")

print("\n Comaprisons:",total_merge)
