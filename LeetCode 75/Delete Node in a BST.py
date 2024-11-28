def deleteNode(root, key):
    if root == None:
        return root

    if key > root.val:
        root.right = deleteNode(root.right, key)
    elif key < root.val:
        root.left = deleteNode(root.left, key)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        
        curr = root.right
        while curr.left != None:
            curr = curr.left
        root.val = curr.val
        root.right = deleteNode(root.right, root.val)
    return root