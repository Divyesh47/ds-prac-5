list1 = [2,4,15,15,25,21,36,53,63,62,72,74,88]
print("List = ",list1)
size = len(list1)
def binary_search(x):
    print("BINARY SEARCHING")
    low = 0
    high = len(list1) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if list1[mid] < x:
            low = mid + 1
        elif list1[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def lsearching(n):
	print("LINEAR SEARCHING")
	if n not in list1:
		print(n,"not in the list")
	else:
		for i in range(size):
			if list1[i]==n:
				print("index of ", n," is ",i)

n = input("Enter (L) for Linear search and  (B) for Binary search \n ")
if n=="L" or n=="l":
	v = int(input("Enter a no. from the list1 "))
	lsearching(v)
elif n=="B" or n=="b":
	v = int(input("Enter a no. from the list1 "))
	print("index of ",v," is ",binary_search(v))
else:
	print("Invalid input")
 39  Practical-6.py
@@ -0,0 +1,39 @@
list1 = [3,14,24,43,54,62,66,72,21,76,80]
print("List = ",list1)
n = len(list1)
def bubbleSort():
    print("Bubble Sorting")
    for i in range(n-1):
        for j in range(0, n-i-1):
            if list1[j] > list1[j+1] :
                list1[j], list1[j+1] = list1[j+1], list1[j]
    print(list1)

def SelectionSort():
	print("Selection Sorting")
	for i in range(n):
		for j in range(i):
			if list1[i]<list1[j]:
				list1[i],list1[j] = list1[j],list1[i]
	print(list1)

def InsertionSort():
    print("Insertion Sorting")
    for i in range(1, n):
        c = list1[i]
        j = i-1
        while j >=0 and c < list1[j] :
                list1[j+1] = list1[j]
                j -= 1
        list1[j+1] = c
    print(list1)

inp = input("Enter (B) for Bubble Sort, (S) for elsection Sort and (I) for Insertion Sort \n")
if inp=="B" or inp=="b":
	bubbleSort()
elif inp=="S" or inp=="s":
	SelectionSort()
elif inp=="I" or inp=="i":
	InsertionSort()
else:
	print("Invalid input") 