def deleteMiddle(head):
    if head.next == None:
        return None
    prev = None
    fastNode = head
    slowNode = head

    while fastNode != None and fastNode.next != None:
        fastNode = fastNode.next.next
        prev = slowNode
        slowNode = slowNode.next
    prev.next = slowNode.next

    return head
