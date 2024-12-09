def orangesRotting(grid):
    def findRotten():
        rotten_list = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rotten_list.append([row, col])
        return rotten_list
    
    rottens = findRotten()
    
    breadth_nodes = [r for r in rottens]
    minutes = 0

    while len(breadth_nodes) > 0:
        arr_size = len(breadth_nodes)
        minutes += 1
        for _ in range(arr_size):
            node = breadth_nodes.pop(0)
            
            # Check left
            row  = node[0]
            col = node[1] - 1
            if (row > -1 and row < len(grid)) and (col > -1 and col < len(grid[0])):
                if grid[row][col] == 1:
                    grid[row][col] = 2
                    breadth_nodes.append([row, col])

            # Check right
            row  = node[0]
            col = node[1] + 1
            if (row > -1 and row < len(grid)) and (col > -1 and col < len(grid[0])):
                if grid[row][col] == 1:
                    grid[row][col] = 2
                    breadth_nodes.append([row, col])
                    

            # Check top
            row  = node[0] - 1
            col = node[1]
            if (row > -1 and row < len(grid)) and (col > -1 and col < len(grid[0])):
                if grid[row][col] == 1:
                    grid[row][col] = 2
                    breadth_nodes.append([row, col])
                    
            
            # Check bottom
            row  = node[0] + 1
            col = node[1]
            if (row > -1 and row < len(grid)) and (col > -1 and col < len(grid[0])):
                if grid[row][col] == 1:
                    grid[row][col] = 2
                    breadth_nodes.append([row, col])
                    
    
    # Check for any fresh oranges
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                return -1
    
    if minutes == 0:
        return 0
    
    return minutes - 1

if __name__ == "__main__":
    grid = [[0]]
    print("Result:",orangesRotting(grid))


    