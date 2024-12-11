class Node:
    #définir un arbre
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def UpdateHeight(self):
        self.height = 0
        if self.left is not None:
            self.height = self.left.height+1
        if self.right is not None and self.right.height+1 > self.height is not None:
            self.height = self.right.height+1

    def getBalance(self):
        lh = -1
        rh = -1
        if self.left is not None:
            lh = self.left.height
        if self.right is not None:
            rh = self.right.height
        return rh-lh

    def find_Max(self):
        # trouver le maximum (fils droit)
        current = self
        while current.right is not None:
            current = current.right
        return current
    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.value)
        if self.right:
            self.right.in_order_traversal()

def insertNode(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insertNode(root.left, value)
    else :
        root.right = insertNode(root.right, value)
    root.UpdateHeight()
    return root
def deleteNode(root, value):
    if root is None:
        return None
    if value < root.value:
        root.left = deleteNode(root.left, value)
        root.UpdateHeight()
        return root
    if value > root.value:
        root.right = deleteNode(root.right, value)
        root.UpdateHeight()
        return root
    if root.left is None and root.right is None:
        return None
    if root.right is None and root.left is not None:
        return root.left
    if root.left is None and root.right is not None:
        return root.right
    max = root.left.find_Max()
    root.value = max.value
    max.value = value
    root.left = deleteNode(root.left, value)
    root.UpdateHeight()
    return root

def LeftRotate(root : Node):
    if root is None or root.right is None:
        return root
    racine = root.right
    root.right = racine.left
    racine.left = root
    root.UpdateHeight()
    racine.UpdateHeight()
    return racine

def RightRotate(root : Node):
    if root is None or root.left is None:
        return root
    racine = root.left
    root.left = racine.right
    racine.right = root
    root.UpdateHeight()
    racine.UpdateHeight()
    return racine

class AVLTree:
    def __init__(self):
        self.root:Node = None

    def balance(self):
        if self.root is None:
            return
        if self.root.left is None and self.root.right is None:
            return
        balance = self.root.getBalance()
        if balance < -1:
            leftBalance = self.root.left.getBalance()
            if leftBalance > 0:
                self.root.left = LeftRotate(self.root.left)
            self.root = RightRotate(self.root)
        if balance > 1:
            rightBalance = self.root.right.getBalance()
            if rightBalance > 0:
                self.root.right = RightRotate(self.root.right)
            self.root = LeftRotate(self.root)

    def insert(self, value):
        self.root = insertNode(self.root, value)
        self.balance()

    def delete(self, value):
        self.root = deleteNode(self.root, value)
        self.balance()
    def display(self):
        self.root.in_order_traversal()


avl = AVLTree()
avl.insert(5)
avl.insert(7)
avl.insert(9)
avl.insert(2)
avl.insert(11)
avl.insert(1)
avl.display()
print()
avl.delete(7)
avl.display()


            #☺☺☺☺☺      ☺☺☺☺☺      ☺☺☺☺☺      ☺☺☺☺☺      ☺☺☺☺☺
