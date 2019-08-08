def searchArray(li,key):
	beg = 0
	end=len(li)-1
	while beg <= end:
		mid = (beg + end)/2
		if (key == li[mid]):
			return 1
		elif (key > li[mid]):
			beg = mid +1
		else :
			end = mid-1
		
	return -1
f= open('req.txt')
testcase =int(f.readline())
for i in range(testcase):
	n,ke = list(map(int,f.readline().split()))
	arr=list(map(int,f.readline().split()))
	print(searchArray(arr,ke))


