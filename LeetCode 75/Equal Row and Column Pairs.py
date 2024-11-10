def equalPairs(grid):
    count = 0
    for arr in grid:
        for j in range(len(grid)):
            temp_arr = []
            for i in range(len(grid[0])):
                temp_arr.append(grid[i][j])
            if temp_arr == arr:
                print("{} | {}".format(temp_arr, arr))
                count += 1
    return count 

if __name__ == "__main__":
    grid = [[3,1,2,2],
            [1,4,4,5],
            [2,4,2,2],
            [2,4,2,2]]
    print("Result:",equalPairs(grid))