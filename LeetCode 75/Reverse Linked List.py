def reverseList(head):
    if head == None or head.next == None:
        return head
    prev = None
    curr = head
    next_node = None

    while curr != None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev