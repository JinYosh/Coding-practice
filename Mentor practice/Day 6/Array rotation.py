def arrRotBF(A, k):
    k = len(A) % k
    for _ in range(k):
        ele = A[0]
        i = 0
        while i < len(A):
            if i + 1 < len(A):
                A[i] = A[i + 1]
            else:
                A[i] = ele
            i += 1

def arrRotNewArrCross(A, k):
    k = k % len(A)
    newArr = [0] * len(A)
    n_i = 0
    o_i = k
    while o_i < len(A):
        newArr[n_i] = A[o_i]
        o_i += 1
        n_i += 1
    o_i = 0
    while o_i < k:
        newArr[n_i] = A[o_i]
        n_i += 1
        o_i += 1
    return newArr

def arrRotInMem(A, k):
    k = k % len(A)
    # Reverse 0 to k - 1 elements
    l = 0
    r = k - 1
    while l < r:
        temp = A[l]
        A[l] = A[r]
        A[r] = temp
        l += 1
        r -= 1
    # Reverse k to len(A) - 1 elements
    l = k
    r = len(A) - 1
    while l < r:
        temp = A[l]
        A[l] = A[r]
        A[r] = temp
        l += 1
        r -= 1
    # Reverse whole arr
    l = 0
    r = len(A) - 1
    while l < r:
        temp = A[l]
        A[l] = A[r]
        A[r] = temp
        l += 1
        r -= 1
    


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6]
    k = 10
    arrRotInMem(A, k)
    print(A)
    #print("Result:",arrRotNewArrCross(A, k))
