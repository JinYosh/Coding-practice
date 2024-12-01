def findCirclNum(isConnected):
    totalNodes = len(isConnected)
    visited = set()
    totalProvinces = 0

    def dfs(i):
        for j in range(totalNodes):
            if isConnected[i][j] == 1 and j not in visited:
                visited.add(j)
                dfs(j)
                

    for i in range(totalNodes):
        if i not in visited:
            totalProvinces += 1
            dfs(i)
    return totalProvinces

if __name__ == "__main__":
    isConnected = [[1,0,0], [0,1,0], [0,0,1]]
    print("Result:",findCirclNum(isConnected))


