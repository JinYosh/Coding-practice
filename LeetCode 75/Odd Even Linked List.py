#def oddEvenList(head):
#    if head.next == None:
#        return head
#    curr = head
#    lastNode = None
#    while curr.next != None:
#        curr = curr.next
#        lastNode = curr
#    prevNode = None
#    curr = head
#    tempLast = lastNode
#    while curr != lastNode:
#        if curr.val % 2 != 0:
#            prevNode = curr
#            curr = curr.next
#        else:
#            if prevNode == None:
#                head = curr.next
#            else:
#                prevNode.next = curr.next
#            tempLast.next = curr
#            curr.next = None
#            tempLast = curr
#            curr = prevNode.next
#    if curr.val % 2 == 0:
#        prevNode.next = curr.next
#        tempLast.next = curr
#        curr.next = None
#    return head
class ListNode:
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if head == None or head.next == None:
        return head
    count = 1
    e_node = None
    o_node = None
    o_head = None
    e_head = None
    curr = head
    while curr != None:
        new_node = ListNode(val=curr.val)
        if count % 2 == None:
            if e_node == None:
                e_head = new_node
                e_node = e_head
            else:
                e_node.next = curr
        else:
            if o_node == None:
                o_head = new_node
                o_node = o_head
            else:
                o_node.next = new_node
        curr = curr.next
        count += 1
    o_node.next = e_head
    return o_head





