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

    # Method to add a node at any index - Indexing starts from 0.
    def insert_at_any_index(self, data, index):
        if index == 0:
            self.insert_at_beginning(data)

        current_node = self.head
        position = 0

        while current_node is not None and position + 1 < index:
            current_node = current_node.next
            position += 1

        if current_node is not None:
            new_node = LinkedListNode(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not valid")

    # Method to remove first node of linked list
    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):
        if self.head is None:
            return
        temp = self.head
        while temp is not None and temp.next.next is not None:
            temp = temp.next
        temp.next = None

    # Method to remove a node from linked list
    def remove_at_any_index(self, index):
        if index == 0:
            self.head = self.head.next

        temp = self.head
        position = 0

        while temp is not None and position + 1 < index:
            position += 1
            temp = temp.next

        if temp is not None:
            temp.next = temp.next.next
        else:
            print("Index is not valid")

    # print method for the linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    linkList = LinkedList()
    print("head of linklist", linkList.head)
    linkList.insert_at_beginning(101)
    linkList.insert_at_end(102)
    linkList.insert_at_beginning(100)
    linkList.insert_at_end(105)
    linkList.insert_at_any_index(104, 3)

    linkList.printList()

    linkList.remove_first_node()
    print("Linklist After removing first node from linklist")
    linkList.printList()

    linkList.remove_last_node()
    print("Linklist After removing last node from linklist")
    linkList.printList()

    linkList.remove_at_any_index(1)
    print("Linklist After removing last node from linklist")
    linkList.printList()
