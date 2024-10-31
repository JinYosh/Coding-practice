def solve(A):
    A.sort()
    for i in range(1, len(A) -1, 2):
        A[i], A[i + 1] = A[i + 1], A[i]
    return A

if __name__ == "__main__":
    A = [4, 3, 7, 8, 6, 2, 1] 
    print("Result:",solve(A))