def leafSimilar(root1, root2):
    list_1 = []
    list_2 = []
    recursion(list_1, root1)
    recursion(list_2, root2)
    return list_1 == list_2
def recursion(list_, root):
    if root.left == None and root.right == None:
        list_.append(root.val)
    else:
        if root.left != None:
            recursion(list_, root.left)
        if root.right != None:
            recursion(list_, root.right)
    
