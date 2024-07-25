# Template for linked list node class
class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data):
        self.data = data
        self.next = None


# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # Method to add a node at begin of Linklist
    def insert_at_beginning(self, data):
        new_node = LinkedListNode(data)  # Create a new node
        new_node.next = self.head  # Next for new node becomes the current head
        self.head = new_node  # Head now points to the new node

    # Method to add a node at end of Linklist
    def insert_at_end(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node

        current_node = self.head
        while current_node.next:  # traverse the list to find the last node
            current_node = current_node.next

        current_node.next = new_node  # Make the new node the next node of the last node

