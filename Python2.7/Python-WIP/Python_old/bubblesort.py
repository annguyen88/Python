def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				temp=  alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
alist = [1, 2, 3, 22, 1000, 24, 0, 23, 4]
bubbleSort(alist)
print(alist)
