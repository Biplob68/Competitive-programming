# Reverse Linklist

def reverseList(head):
    pre_node = None
    current_node = head

    while current_node:
        next_node = current_node.next
        current_node.next = pre_node
        pre_node = current_node
        current_node = next_node

    return pre_node
