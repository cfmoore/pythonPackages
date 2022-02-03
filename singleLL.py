class SingleLL:

    # Initial definition for singly linked lists and Doubly Linked list
    def __init__(self, info):
        self.info = info  # Whatever information to keep here
        self.next = None  # Reference to next node in list

    # Get the information stored in node
    def get_info(self):
        return self.info

    # Set the information in the node
    # Used for overwriting data
    def set_info(self, info):
        self.info = info

    # Get the next node in the list
    # SHOULD RETURN NONE AT END OF LIST
    def get_next(self):
        return self.next

    # Set the next node in the list
    def set_next(self, new_node):
        self.next = new_node


    # Add node to the list
    def add_node(self, info):
        if self.get_next() is None:
            self.set_next(SingleLL(info))
        else:
            self.get_next().add_node(info)

    # Printer of list
    def print_nodes(self):
        print(self.get_info(), ' ', end='')
        if self.get_next() is not None:
            self.get_next().print_nodes()
        else:
            print()
            return



