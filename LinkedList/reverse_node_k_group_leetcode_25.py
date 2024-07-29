import linklist_implementation


def reverseKGroup(head, k):
    temp = head
    cnt = 0
    while temp is not None:
        temp = temp.next
        cnt += 1

    segment = cnt // k

    current_node = head
    pre = None

    index = 0
    while index < k:
        next_node = current_node.next
        current_node.next = pre
        pre = current_node
        current_node = next_node
        index += 1

    left = head
    temp_left = current_node
    segment -= 1

    if segment == 0 and current_node is not None:
        left.next = current_node

    head = pre
    while segment > 0 and current_node is not None:
        index = 0
        pre = None
        while index < k:
            next_node = current_node.next
            current_node.next = pre
            pre = current_node
            current_node = next_node
            index += 1

        right = pre
        left.next = right
        left = temp_left
        temp_left = current_node

        if current_node is not None:
            left.next = current_node
        segment -= 1


if __name__ == '__main__':
    linkList = linklist_implementation.LinkedList()
    linkList.insert_at_beginning(1)
    linkList.insert_at_end(2)
    linkList.insert_at_end(3)
    linkList.insert_at_end(4)
    linkList.insert_at_end(5)
    linkList.insert_at_end(6)
    linkList.insert_at_end(7)
    linkList.insert_at_end(8)
    linkList.insert_at_end(9)
    linkList.insert_at_end(10)

    reverseKGroup(linkList.head, 3)
    linkList.printList()
