class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level
    def printTree(self):
        spaces = ' ' * self.getLevel() * 3
        spaces += "|__" if self.parent else ""
        print(spaces + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.printTree()
    
def buildProductTree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.addChild(TreeNode("HP"))
    laptop.addChild(TreeNode("Apple"))
    laptop.addChild(TreeNode("Lenevo"))

    fridge = TreeNode("Fridge")
    fridge.addChild(TreeNode("Samsung"))
    fridge.addChild(TreeNode("Whirpool"))
    fridge.addChild(TreeNode("Hair"))

    smartphone = TreeNode("Smart Phone")
    smartphone.addChild(TreeNode("Samsung"))
    smartphone.addChild(TreeNode("Apple"))
    smartphone.addChild(TreeNode("Xiomi"))

    root.addChild(child=fridge)
    root.addChild(child=laptop)
    root.addChild(child=smartphone)

    return root
if __name__ == "__main__":
    root = buildProductTree()
    root.printTree()
    
    