def eveNumsrange(A, Q):
    ans_list = []
    PE = [1 if A[0] % 2 == 0 else 0]
    for i in range(1, len(A)):
        total = PE[i - 1] + (1 if A[i] % 2 == 0 else 0)
        PE.append(total)
    for L, R in Q:
        total_even = PE[R] - (PE[L - 1] if L - 1 > -1 else 0)
        ans_list.append(total_even)
    return ans_list

if __name__ == "__main__":
    A = [2,1,8,3,9,6]
    Q = [[0,3],
         [3,5],
         [1,3],
         [2,4]]
    print("Result:",eveNumsrange(A, Q))