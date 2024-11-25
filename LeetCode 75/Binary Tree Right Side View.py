def rightView(root):
    if root == None:
        return []
    queue = []
    right_view = []
    queue.append(root)
    right_view.append(root.val)
    while len(queue) > 0:
        len_queue = len(queue)
        for _ in range(len_queue):
            node = queue.pop(0)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        if len(queue) > 0:
            right_view.append(queue[-1].val)
    return right_view