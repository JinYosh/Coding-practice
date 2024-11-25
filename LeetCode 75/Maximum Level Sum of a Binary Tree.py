def maxLevelSum(root):
    if root == None:
        return 0
    level = 0
    queue = [root]
    maxSum = - ((10 ** 9) + 7)
    sumLevel = 0
    while len(queue) > 0:
        len_queue = len(queue)
        sum_list = []
        for _ in range(len_queue):
            node = queue.pop(0)
            sum_list.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        sum_ = sum(sum_list)
        level += 1
        if sum_ > maxSum:
            maxSum = sum_
            sumLevel = level
    return sumLevel


