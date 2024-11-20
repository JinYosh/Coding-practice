def goodNodes(root):
    leftCount = recursion(root.left, root.val) if root.left != None else 0
    rightCount = recursion(root.right, root.val) if root.right != None else 0
    return leftCount + rightCount + 1

def recursion(root, maxNum):
    if root == None:
        return 0
    if root.val >= maxNum: 
        maxNum = root.val
        return 1 + recursion(root.left, maxNum) + recursion(root.right, maxNum)
    else:
        return recursion(root.left, maxNum) + recursion(root.right, maxNum)


