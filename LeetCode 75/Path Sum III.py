def pathSum(root, targetSum):
    total = 0
    def helper(node, curr):
        if node == None:
            return 
        helper(node.left, curr + node.val)
        helper(node.right, curr + node.val)
        if curr + node.val == targetSum:
            total += 1
    def dfs(node):
        if node == None:
            return 
        helper(node, 0)
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return total

def pathSum1(root, targetSum):
    total = 0
    lookup = defaultdict(int)
    lookup[targetSum] = 1

    def dfs(node, rootSum):
        if not node:
            return
        root_sum += node.val
        total = lookup[rootSum]
        lookup[rootSum + targetSum] += 1
        dfs(node.left, rootSum)
        dfs(node.right, rootSum)
        lookup[rootSum + targetSum] -= 1
    dfs(root, 0)
    return total