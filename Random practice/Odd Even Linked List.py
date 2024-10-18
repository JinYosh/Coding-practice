def oeListIterative(head):
    o_head = None
    o_prev = None
    e_head = None
    e_prev = None
    while head:
        data = head.next
        if data % 2 != 0:
            if o_head == None:
                o_head = head
                o_prev = o_head
            else:
                o_prev.next = head
                o_prev = head
        else:
            if e_head == None:
                e_head = head
                e_prev = e_head
            else:
                e_prev.next = head
                e_prev = head
        head = head

    e_prev.next = o_head

    return e_head
        

def oeListAlternate(head):
    o_node = head
    e_node = head.next
    temp = head
    while temp.next:
        bt_node = None
        #data = temp.val
        if temp.next.next:
            bt_node = temp.next
            temp.next = temp.next.next
        temp = bt_node
        #data = temp.val
    #if data % 2 == 0:
    temp.next = e_node
    return o_node
        
    



