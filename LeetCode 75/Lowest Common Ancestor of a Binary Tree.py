def lowestCommonAncestor(root, p, q):

    # For BST
    #curr = root
    #while curr != None:
    #    if p.val > curr.val and q.val > curr.val:
    #        curr = curr.right
    #    elif p.val < curr.val and q.val < curr.val:
    #        curr = curr.left
    #    else:
    #        return curr.val
    
    if not root:
        return None
    if root == p or root == q:
        return root
    l = lowestCommonAncestor(root.left, p, q)
    r = lowestCommonAncestor(root.right, p, q)
    if l != None and r != None:
        return root
    else:
        return l or r


