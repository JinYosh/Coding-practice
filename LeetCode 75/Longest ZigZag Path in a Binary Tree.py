def longestZigZag(root):
    queue = collections.deque([])
    if root.left != None:
        queue.append((root.left, "Left", 1))
    if root.right != None:
        queue.append((root.right, "Right", 1))
    best = 0
    while queue:
        node, frm, steps = queue.popleft()
        best = max(best, steps)
        if node.left:
            if frm == "Right":
                queue.append((node.left, "Left", steps + 1))
            else:
                queue.append((node.left, "Left", 1))
        if node.right:
            if frm == "Left":
                queue.append((node.right, "Right", steps + 1))
            else:
                queue.append((node.right, "Right", 1))
    return best 