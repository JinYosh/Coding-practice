def sumQueryBF(A, B):
    ans_list = []
    for L, R in B:
        sum_ = 0
        for i in range(L, R + 1, 1):
            sum_ += A[i]
        ans_list.append(sum_)
    return ans_list

def sumQueryPS(A, B):
    PS = [A[0]]
    ans_list = []
    for i in range(1, len(A)):
        PS.append(PS[i-1] + A[i])
    for L, R in B:
        sum_ = PS[R] - (PS[L-1] if L-1 >= 0 else 0)
        ans_list.append(sum_)
    return ans_list

if __name__ == "__main__":
    A = [2,2,2]
    B = [[0,0],
         [1,2],]
    
    print("Result:",sumQueryBF(A, B))