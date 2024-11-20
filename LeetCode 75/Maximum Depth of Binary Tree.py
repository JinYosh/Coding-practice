def maxDepth(root):
    if root == None:
        return 0
    
    l_height = 0
    r_height = 0

    l_height = 1 + maxDepth(root.left)
    r_height = 1 + maxDepth(root.right)
    
    return max(l_height, r_height)

