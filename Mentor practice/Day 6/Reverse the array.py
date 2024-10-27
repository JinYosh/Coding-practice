def reverseArray(A):
    l = 0
    r = len(A) - 1
    while l < r:
        temp = A[l]
        A[l] = A[r]
        A[r] = temp
        l += 1
        r -= 1
    return A

if __name__ == "__main__":
    A = [1,2,3,4,5]
    print("Result:",reverseArray(A))