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
    
if __name__ == '__main__':
    print("Hello World!")
    boxOne = Box(3,6,1)
    print(boxOne)