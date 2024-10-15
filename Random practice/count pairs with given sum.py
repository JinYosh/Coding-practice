#def solve(A, s):
#    total_pairs = 0
#    for i in range(len(A)):
#        for j in range(i+1, len(A)):
#            if A[i] + A[j] == s:
#                total_pairs += 1
#    return total_pairs

def solve(A, s):
    total_pairs = 0
    HM = {}
    for i in range(len(A)):
        diff = s - A[i]
        if diff in HM.keys():
            freq = HM[diff]
            total_pairs += freq
        if A[i] in HM.keys():
            HM[A[i]] += 1
        else:
            HM[A[i]] = 1
    return total_pairs

if __name__ == "__main__":
    A = [1,1,5,5]#[1, 5, 7, -1, 5]
    s = 6
    print("Result:",solve(A, s))