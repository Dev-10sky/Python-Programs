import time

class Box:

    def __init__(self, h, l, val):
        self.height = h
        self.length = l
        self.value = val
    
    def getArea(self):
        return self.height * self.length

    def __str__(self):
        top = ("+" * (self.length)) + "\n" 
        side = ("+" + (" " * (self.length - 2)) + "+") + "\n"
        sides = side * self.height
        res = top + sides + top
        return res

class Display:

    def __init__(self, maxVal, arrLen) -> None:
        self.max = maxVal
        self.length = arrLen
        self.window = None
    
    def makeDisplay(self):
        self.window = [["  " for n in range(self.length)] for x in range(self.max)]

    def printDisplay(self):
        line = len(self.window[0])
        for n in self.window:
            temp = ''.join(n)
            print(temp)
        print("--"*line)
    
    def updateDisplay(self,arr):
        for val in range(len(arr)):
            for row in range(len(self.window)):
                res = (len(self.window) - (row)) - arr[val]
                if res <= 0:
                    self.window[row][val] = "[]"
                else:
                    self.window[row][val] = "  "


if __name__ == '__main__':
    print("Hello World!")
    boxOne = Box(3,6,1)
    print(boxOne)