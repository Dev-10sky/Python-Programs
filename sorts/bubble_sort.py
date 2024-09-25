import math

def printDisplay(a):
	for n in a:
		temp = ''.join(n)
		print(temp)
	print("<----------------------------------------------->")

def makeDisplay(maxval,arrlen):
	temp = [["  " for n in range(arrlen)] for x in range(maxval)]
	return temp

def updateDisplay(display,arr):
	for val in range(len(arr)):
		for row in range(len(display)):
			res = (len(display) - (row)) - arr[val]
			if res <= 0:
				display[row][val] = "[]"
			else:
				display[row][val] = "  "
				
def bubble(lst):
	for m in range(len(lst)-1):
		for n in range(len(lst)-1):
			if lst[n] > lst[n + 1]:
				lst[n], lst[n + 1]  = lst[n + 1], lst[n]
	return lst

def bubbleDisplay(arr):
	currMax = max(arr)
	size = len(arr)
	window = makeDisplay(currMax,size)
	print(arr)
	updateDisplay(window,arr)
	printDisplay(window)
	for m in range(len(arr)-1):
		for n in range(len(arr)-1):
			if arr[n] > arr[n + 1]:
				arr[n], arr[n + 1]  = arr[n + 1], arr[n]
				updateDisplay(window,arr)
				printDisplay(window)
	return arr

if __name__ == '__main__':
	l = [7, 4, 8, 6, 2 ,1 ,9, 10, 5]
	print(bubbleDisplay(l))