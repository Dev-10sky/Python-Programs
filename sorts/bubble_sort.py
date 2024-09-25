import math
from box.box import Display

def bubble(lst):
	for m in range(len(lst)-1):
		for n in range(len(lst)-1):
			if lst[n] > lst[n + 1]:
				lst[n], lst[n + 1]  = lst[n + 1], lst[n]
	return lst

def bubbleDisplay(arr,display:Display):
	display.makeDisplay()
	display.updateDisplay(arr)
	display.printDisplay()
	for m in range(len(arr)-1):
		for n in range(len(arr)-1):
			if arr[n] > arr[n + 1]:
				arr[n], arr[n + 1]  = arr[n + 1], arr[n]
				display.updateDisplay(arr)
				display.printDisplay()
	return arr

if __name__ == '__main__':
	l = [7, 4, 8, 6, 2 ,1 ,9, 10, 5]
	dispOne = Display(max(l),len(l))
	print(bubbleDisplay(l,dispOne))