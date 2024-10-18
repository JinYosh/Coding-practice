# Using iteration
def solve(head):
    prevNode = None
    while head:
        nextNode = head.next
        head.next = prevNode
        prevNode = head
        head = nextNode
    return prevNode

# Using stack
def solve(head):
    temp = head 
    stack = []
    while temp.next:
        stack.append(temp)
        temp = temp.next
    
    head = temp
    while len(stack) > 0:
        temp.next = stack.pop()
        temp = temp.next
    temp.next = None
    return head

def reverseRecursive(head):
    if head == None or head.next == None:
        return head
    newNode = reverseRecursive(head.next)
    head.next.next = head
    head.next = None
    return newNode