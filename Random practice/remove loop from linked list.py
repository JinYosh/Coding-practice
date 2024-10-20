
def iterationApproach(head):
    set_ = set()
    temp = head
    while temp:
        if temp in set_:
            temp.next = None
            return head
        temp = temp.next
    return head


# Floyd's cycle detection
def floydDetection(head):
    slowptr = head
    fastptr = head
    while fastptr:
        if fastptr == slowptr:
            break
        else:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
    
    slowptr = head
    
    while fastptr:
        if slowptr.next == fastptr.next:
            fastptr.next = None
            break
        slowptr = slowptr.next
        fastptr = fastptr.next
    return head

