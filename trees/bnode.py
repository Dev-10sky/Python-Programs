



class Node:

    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

    def addleft(self, node):
        self.left = node

    def addright(self, node):
        self.right = node

    def makenode(self, value):
        return Node(value)

    def insert(self, value):
        if self == None:
            return None
        elif value <= self.value:
            if self.left == None:
                self.left = self.makenode(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = self.makenode(value)
            else:
                self.right.insert(value)
    def getprint(self):
        msg = "<" + str(self.value) + ">"
        if self.left != None:
            msg += " Child of ["+ str(self.value)+ "]:" + self.left.getprint()
        if self.right != None:
            msg += " Child of ["+ str(self.value)+ "]:" + self.right.getprint()
        return msg

    def __str__(self):
        return self.getprint()


if __name__ == '__main__':
    nodeOne = Node(2)
    print(nodeOne)
    nodeOne.insert(5)
    print(nodeOne)
    nodeOne.insert(1)
    print(nodeOne)
    nodeOne.insert(4)
    print(nodeOne)
