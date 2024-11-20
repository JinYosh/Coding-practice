def pairSum(head):
    list_ = []
    curr = head
    while curr != None:
        list_.append(curr.val)
        curr = curr.next
    l = 0
    r = len(list_) - 1
    max_sum = float('inf')
    while l < r:
        sum_ = list_[l] + list_[r]
        max_sum = max(max_sum, sum_)
        l += 1
        r -= 1
    return max_sum