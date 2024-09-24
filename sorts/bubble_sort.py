import math

def printDisplay(a):
	for n in a:
		print(n)

def makeDisplay(maxval,arrlen):
	return [[0]*(arrlen)]*(maxval)

def updateDisplay(display,arr):
	for val in range(len(arr)):
		for row in range(len(display)):
			res = (len(display) - (row)) - arr[val]
			if res <= 0:
				display[row][val] = 1
				
def bubble(lst):
	for m in range(len(lst)-1):
		for n in range(len(lst)-1):
			if lst[n] > lst[n + 1]:
				lst[n], lst[n + 1]  = lst[n + 1], lst[n]
	return lst




if __name__ == '__main__':
	l = [7, 4, 8, 6, 2 ,1 ,9, 10, 5]
	print(l)
	# print(bubble(l))
	newDisplay = makeDisplay(max(l), len(l))
	printDisplay(newDisplay)
	updateDisplay(newDisplay,l)
	print("<----------------------------------------------->")
	printDisplay(newDisplay)