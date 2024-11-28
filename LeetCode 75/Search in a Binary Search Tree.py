def searchBST(root, p):
    node = root
    while True:
        if not node:
            return None
        if p == node.val:
            break
        if p < node.val:
            node = node.left
        elif p > node.val:
            node = node.right
    return node

def searchBST1(root, p):
    if root == None:
        return None
    if p == root.val:
        return root
    if p < root.val:
        return searchBST(root.left, p)
    elif p > root.val:
        return searchBST(root.right, p)



