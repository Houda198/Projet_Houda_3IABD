class Cell:
    def __init__(self, value: int):
        self.value = value
        self.previous = None
        self.next = None


class MyList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    # fonction pour insérer value dans la liste
    def insert_next(self, value, element: Cell):
        new_element = Cell(value)
        # on vérifie si la liste est vide on donne la valeur new_element pour la première cell de la liste
        # vu qu'on a une seule valeur le début = la fin
        if self.size == 0:
            self.head = new_element
            self.tail = new_element
        else:
            # faire l'insertion quand la liste n'est pas vide
            new_element.next = element.next
            new_element.previous = element
            # si la cell n'a pas de valeur suivante je crée un (nouveau) new_element qui est dernier de la liste
            if element.next is None:
                self.tail = new_element
                # sinon on créée une nouvelle cell entre 2 cells et mettre à jour
                # la valeur que prend cette nouvelle cell
            else:
                element.next.previous = new_element
            element.next = new_element
        self.size += 1

    def insert_previous(self, value, element: Cell):
        new_element = Cell(value)

        if self.size == 0:
            self.head = new_element
            self.tail = new_element

        else:
            new_element.next = element
            new_element.previous = element.previous

            if element.previous is None:
                self.head = new_element
            else:
                element.previous.next = new_element
            element.previous = new_element
        self.size += 1

    def remove(self, element: Cell):
        if element == self.head:
            # dans le cas où je supprime le premier element
            self.head = element.next
            if self.head is None:
                self.tail = None
            else:
                element.next.previous = None
        # dans le cas où je veux supprimer un autre element à part le premier
        else:
            element.previous.next = element.next
            if element.next is None:
                self.tail = element.previous
            else:
                element.next.previous = element.previous
        self.size -= 1

    def display(self):
        element = self.head
        print("[", end="")
        for i in range(self.size):
            print(element.value, end=", ")
            element = element.next
        print("]")

my_list = MyList()

my_list.insert_next(5, None)
my_list.display()

my_list.insert_next(value = 12, element = my_list.tail)
my_list.display()

my_list.insert_previous(value = 32, element = my_list.tail)
my_list.display()

my_list.remove(my_list.head)
my_list.display()

my_list.remove(my_list.tail)
my_list.display()
