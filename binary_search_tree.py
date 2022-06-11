from ast import Delete
from tkinter.messagebox import NO


class BinaryNodeSearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def addChild(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinaryNodeSearchTree(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinaryNodeSearchTree(data)
    def inorderTraversal(self):
        elements = []
        if self.left:
            elements+= self.left.inorderTraversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.inorderTraversal()
        return elements
    def Search(self,val):
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.Search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.Search(val)
            else:
                return False

    def min(self):
        if self.left == None:
            return self.data
        return self.left.min()
    
    def max(self):
        if self.right == None:
            return self.data
        return self.right.min()

    def Delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.Delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.Delete(val)
        else:
            if self.left == None and self.right == None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min = self.right.min()
            self.data = min
            self.right.Delete(min)
        return self

def buildTree(elements):
    root = BinaryNodeSearchTree(elements[0])
    elements.pop(0)
    for i in elements:
        root.addChild(i)
    return root

if __name__ == "__main__":
    ele = [20,40,12,4,7,454,2,21]
    tree = buildTree(ele)
    tree.Delete(40)
    print(tree.inorderTraversal())
    print(tree.Search(4))
    print(tree.Search(5))

