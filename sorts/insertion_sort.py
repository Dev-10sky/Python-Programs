import time
from tqdm import tqdm
from ..box.box import Display





def insertion_sort(lst):
    for n in range(1,len(lst)):
        currval = lst[n]
        m = n - 1
        while m >= 0 and currval < lst[m]:
            lst[m + 1] = lst[m]
            m -=1
        lst[m + 1] = currval

def insertion_display(lst, display: Display):
    display.makeDisplay()
    display.updateDisplay(lst)
    display.printDisplay()
    for n in range(1,len(lst)):
        currval = lst[n]
        m = n - 1
        while m >= 0 and currval < lst[m]:
            lst[m + 1] = lst[m]
            m -=1
        lst[m + 1] = currval
        display.updateDisplay(lst)
        display.printDisplay()

if __name__ == "__main__":
    l = [7, 4, 8, 6, 2 ,1 ,9, 10, 5, 3, 15]
    dispOne = Display(max(l),len(l))
    print(f"Before: {l}".format(l))
    insertion_sort(l)
    print(f"After: {l}".format(l))
    print("<---display sort--->")
    l = [7, 4, 8, 6, 2 ,1 ,9, 10, 5, 3, 15]
    print(f"Before: {l}".format(l))
    insertion_display(l,dispOne)
    print(f"After: {l}".format(l))