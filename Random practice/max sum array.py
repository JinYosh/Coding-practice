import copy
def solve(A):
    maxEnding = 0
    res = None
    max_list = []
    temp_list = []
    for i in range(len(A)):
        maxEnding += A[i]
        temp_list.append(A[i])
        if maxEnding < 0:
            if res == None or maxEnding > res:
                res = maxEnding
                max_list = copy.deepcopy(temp_list)
            temp_list = []
            maxEnding = 0
        elif res == None or maxEnding > res:
            res = maxEnding
            max_list = copy.deepcopy(temp_list)
    return (max_list, res)

if __name__ == "__main__":
    A = [-2,1,-3,4,-1,2,1,-5,4]
    print("Result:",solve(A))

                
