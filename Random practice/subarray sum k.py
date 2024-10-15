def solve(A, k):
    PS_ = [A[0]]
    for i in range(1, len(A)):
        PS_.append(A[i] + PS_[i - 1])
    print("PS:",PS_)
    HM = {}
    HM[0] = 1
    total_sa = 0
    for i in range(len(PS_)):
        diff = PS_[i] - k
        if diff in HM.keys():
            total_sa += HM[diff]

        if PS_[i] in HM.keys():
            HM[PS_[i]] += 1
        else:
            HM[PS_[i]] = 1
        print("HM",HM)
        
    return total_sa

if __name__ == "__main__":
    A = [1, 3, 5] #[9, 4, 20, 3, 10, 5]#[10, -2, 2, -20, 10] #[1, -1, 1, 1, 1, 1]
    k = 2 #33 #-10 #3
    print("Result:",solve(A, k))


