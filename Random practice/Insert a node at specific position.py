def insertAtPos(head, data, position):
    newNode = Node()
    newNode.data = data
    newNode.next = None
    if position == 0:
        newNode.next = head
        return newNode
    curr = head
    prev = None
    curr_i = 0
    while curr:
        if curr_i == position:
            prev.next = newNode
            newNode.next = curr
        prev = curr
        curr = curr.next
        curr_i += 1 
    if curr_i <= position:
        prev.next = newNode
    return head