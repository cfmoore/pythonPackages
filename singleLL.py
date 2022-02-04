############################################################################
# singleLL.py
# Author: Charles (Chad) Moore
# V 1.0
#   |- v 1.5 will have ability to remove nodes
#
# A singly linked list to hold data
# User needs to just keep track of head of list
# Author recommends once head of list is created, assign a temp variable
# to hold the head.
#
# V 1.0 2/3/2022
############################################################################
class SingleLL:

    # Initial definition for singly linked lists
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
        return

    # Get the next node in the list
    # SHOULD RETURN NONE AT END OF LIST
    def get_next(self):
        return self.next

    # Set the next node in the list
    def set_next(self, new_node):
        self.next = new_node
        return

    # Add node to the list
    def add_node(self, info):
        if self.get_next() is None:
            self.set_next(SingleLL(info))
            return
        else:
            self.get_next().add_node(info)

    # Remove a node from the list
    # @info the node to be removed
    # del will delete the memory allocation, to free memory
    def remove_node(self, info):
        if self.get_next() is not None:
            if self.get_next().get_info() is info:
                temp = self.get_next()
                self.set_next(temp.get_next())
                del temp
                return
            else:
                self.get_next().remove_node(info)
        else:
            print('Node does not exist or node is head, try remove_head()')
            return

    # Function to remove the head
    # @self is the head
    # will make next node in list head
    # returns the next node as head
    # deletes head from memory for memory management
    def remove_head(self):
        temp = self.get_next()
        del self
        self = temp
        del temp
        return self

    # Printer of list
    def print_nodes(self):
        print(self.get_info(), ' ', end='')
        if self.get_next() is not None:
            self.get_next().print_nodes()
        else:
            print()
            return

    # Add Queue functionality to singly linked list
    push = add_node
    pop = remove_head



