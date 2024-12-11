class Node:
    # définir un arbre
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # fonction pour inserer des noeuds
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.value)
        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.value)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.value)

    def search(self, value):
        # recherche dans un arbre
        if self is None:
            return 0
        if self.value == value:
            return 1
        if value < self.value:
            if self.left is not None:
                return self.left.search(value)
            else:
                return 0
        else:
            if self.right is not None:
                return self.right.search(value)
            else:
                return 0

    def find_Min(self):
        # trouver le minimum (fils gauche)
        current = self
        while current.left is not None:
            current = current.left
        return current.value

    def find_Max(self):
        # trouver le maximum (fils droit)
        current = self
        while current.right is not None:
            current = current.right
        return current.value

    # fonction pour supprimer un element d'un arbre
    def delete(self, value):
        if self is None:
            return self
        if value < self.value:
            if self.left is not None:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right is not None:
                self.right = self.right.delete(value)
        else:
            # arbre sans fils
            if self.left is None and self.right is None:
                return None
            # arbre avec un seul fils
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            # arbre avec 2 fils
            min_right_node = self.right.find_Min(value)
            self.value = min_right_node.value
            self.right = self.right.delete(min_right_node.value)
        return self

    # parcours en largeur
    def breadth(self):
        queue = []
        if self.value is not None:
            queue.append(self)
            while queue:
                # supprime les élèments de la file jusqu'à ce qu'elle sit vide
                current_node = queue.pop(0)
                print(current_node.value)
                # ajout de fils gauche et droit s'ils existent
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)

    # taille d'un arbre
    def treeSize(self):
        if self is None:
            return 0
        else:
            size = 1
            if self.left:
                size += self.left.treeSize()
            if self.right:
                size += self.right.treeSize()
        return size

    # Hauteur d'un arbre
    def treeHeigtht(self):
        if self is None:
            return 0
        leftHeight = 0
        if self.left:
            leftHeight = self.left.treeHeigtht()
        rightHeight = 0
        if self.right:
            rightHeight = self.right.treeHeigtht()
        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1

    # nombre de feuilles d'un arbre
    def leafsCount(self):
        if self is None:
            return 0
        if self.left is None and self.right is None:
            return 1
        else:
            leafs = 0
            if self.left:
                leafs += self.left.leafsCount()
            if self.right:
                leafs += self.right.leafsCount()
            return leafs


tree = Node(6)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(19)
tree.insert(29)
tree.insert(11)
tree.insert(4)
tree.insert(2)

# print(tree.leafsCount())
# tree.in_order_traversal()
print(tree.find_Min())
# print(tree.find_Max(tree))

tree = Node(10)
tree.left = Node(5)
tree.right = Node(15)
tree.left.left = Node(3)
tree.left.right = Node(7)
tree.right.left = Node(12)
tree.right.right = Node(18)
