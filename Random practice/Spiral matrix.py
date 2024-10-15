def solve(A):
    sp_mat = [[0 for _ in range(A)] for _ in range(A)]
    I = i = J = j = 0
    k = A - 1
    num = 1
    while k > 2:
        i = I
        j = J
        # top
        while j < k:
            sp_mat[i][j] = num
            num += 1
            j += 1

        # right
        while i < k:
            sp_mat[i][j] = num
            num += 1
            i += 1
        # bottom
        while j > J:
            sp_mat[i][j] = num
            num += 1
            j -= 1
        # left
        while i > I:
            sp_mat[i][j] = num
            num += 1
            i -= 1

        printMat(sp_mat)
        print("I : {} | J : {} | k : {}\n".format(I, J, k))
        
        # change vars
        
        k -= 1
        I += 1
        J += 1
        
    if A % 2 != 0:
        print(I, J)
        sp_mat[I][J] = num
    return sp_mat

def printMat(sp_mat):
    for arr in sp_mat:
        print(arr)
    
    

if __name__ == "__main__":
    A = 5
    result = solve(A)
    for arr in result:
        print(arr)
    #print("Result:",solve(A))