def iterative(head, key):
    if head == None:
        return head
    prev = None
    curr = head
    while curr:
        if curr.val == key:
            if prev == None:
                head = curr.next
            else:
                prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
    return head