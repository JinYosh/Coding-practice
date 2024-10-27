def SumQuery(A, Q):
    PS = [A[0]]
    for i in range(1, len(A)):
        PS.append(PS[i-1] + A[i])
    ans_list = []
    for L, R in Q:
        sum_ = PS[R] - (PS[L-1] if (L - 1) >= 0 else 0 )
        ans_list.append(sum_)
    return ans_list

if __name__ == "__main__":
    A = [2, 2, 2]
    Q = [[0,0],
         [1,2]]
    print("Result:",SumQuery(A, Q))