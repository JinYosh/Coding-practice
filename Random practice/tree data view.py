def displayTree(node):
    if node != None:
        displayTree(node.left)
        print(node.val)
        displayTree(node.right)
