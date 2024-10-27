def prodArray(A):
    prod = 1
    for i in range(len(A)):
        prod *= A[i]
    new_arr = [0 for _ in range(len(A))]
    for i in range(len(A)):
        new_arr[i] = prod // A[i]
    return new_arr

def prodArray1(A):
    PF = []
    p = 1
    for i in range(len(A)):
        p *= A[i]
        PF.append(p)
    SF = []
    p = 1
    for i in range(len(A) - 1, -1, -1):
        p *= A[i]
        SF.append(p)
    ans_list = []
    for i in range(len(A)):
        L = i - 1
        R = i + 1
        prod = (PF[L] if L > -1 else 1) * (PF[R] if R < len(A) else 1)
        ans_list.append(prod)
    return ans_list
''
if __name__ == "__main__":
    A = [1,2,3,4,5]
    print("Result:",prodArray(A))