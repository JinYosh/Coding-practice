#def solve(A, t):
#    set_ = set()
#    for i in range(len(A)):
#        for j in range(i+1, len(A)):
#            diff = t - (A[i] + A[j])
#            if diff in set_:
#                return [A[i], A[j], diff]
#            set_.add(A[i])
#            set_.add(A[j])
#    return False

def solve(A, t):
    A.sort()
    for i in range(0, len(A) - 1, 1):
        l = i + 1
        r = len(A) - 1
        while (l < r):
            curr_sum = A[i] + A[l] + A[r]
            if curr_sum == t:
                return [A[i], A[l], A[r]]
            elif curr_sum < t:
                l += 1
            else:
                r -= 1
    return False

if __name__ == "__main__":
    A = [12, 3, 4, 1, 6, 9]
    t = 24
    print("Result:",solve(A, t))