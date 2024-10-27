def goodPairBF(A, b):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == b:
                return 1
    return 0

def goodPairSet(A, b):
    set_ = set()
    for i in range(len(A)):
        diff = b - A[i]
        if diff in set_:
            return 1
        else:
            set_.add(A[i])
    return 0


if __name__ == "__main__":
    A = [1,2,2]
    b = 4
    print("Result:",goodPairSet(A, b))