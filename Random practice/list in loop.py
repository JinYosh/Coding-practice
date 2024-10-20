def iterativeSet(head):
    set_ = set()
    while head:
        if head in set_:
            return False
        set_.add(head)
        head = head.next
    return True

def twoPointer(head):
    if head.next == None:
        return False
    slowpt = head
    normpt = head.next
    count_diff = 1
    diff = 1
    while normpt:
        if slowpt == normpt:
            return True
        if count_diff == diff:
            slowpt = slowpt.next
            count_diff = 0
            diff += 1
        count_diff += 1
        normpt = normpt.next
    return False

def twoPointer2(head):
    slowPtr = head
    fastPtr = head
    while slowPtr and fastPtr and fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        if slowPtr == fastPtr:
            return True
    return False


        